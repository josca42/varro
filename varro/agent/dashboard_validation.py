from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlsplit

import pandas as pd
import plotly.graph_objects as go
from sqlalchemy.engine import Engine

from varro.agent.workspace import user_workspace_root
from varro.dashboard.executor import (
    clear_query_cache,
    execute_options_query,
    execute_output,
    execute_query,
)
from varro.dashboard.loader import Dashboard, load_dashboard, load_outputs
from varro.dashboard.parser import parse_dashboard_md, extract_filters, ContainerNode, ComponentNode
from varro.dashboard.filters import SelectFilter
from varro.dashboard.models import Metric
from varro.db.db import dst_read_engine as default_engine

STRUCTURE_ERROR_PREFIXES = (
    "Missing queries/ folder in ",
    "Missing outputs.py in ",
    "Missing dashboard.md in ",
    "No .sql files in ",
)


@dataclass
class DashboardValidationResult:
    url: str
    unfiltered: bool | None = None
    queries: dict[str, int] = field(default_factory=dict)
    outputs: dict[str, str] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    query_errors: list[str] = field(default_factory=list)
    output_errors: list[str] = field(default_factory=list)
    pending_reason: str | None = None

    @property
    def pending(self) -> bool:
        return self.pending_reason is not None

    @property
    def has_errors(self) -> bool:
        return bool(self.query_errors or self.output_errors)

    def payload(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "url": self.url,
            "unfiltered": self.unfiltered,
            "queries": self.queries,
            "outputs": self.outputs,
            "warnings": self.warnings,
        }
        if self.pending_reason:
            payload["pending_reason"] = self.pending_reason
        return payload


def parse_dashboard_url(url: str) -> tuple[str, str]:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc:
        raise ValueError("url must be app-relative and start with '/'")
    if not parsed.path.startswith("/"):
        raise ValueError("url must start with '/'")

    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) != 2 or parts[0] != "dashboard" or not parts[1]:
        raise ValueError("url must match /dashboard/{slug}")

    return parts[1], parsed.query


def parse_dashboard_filters(dash: Dashboard, query: str) -> dict[str, Any]:
    query_params = dict(parse_qsl(query, keep_blank_values=True))
    values: dict[str, Any] = {}
    for filter_def in dash.filters:
        values.update(filter_def.parse_query_params(query_params))
    return values


def default_dashboard_filters(dash: Dashboard) -> dict[str, Any]:
    values: dict[str, Any] = {}
    for filter_def in dash.filters:
        values.update(filter_def.parse_query_params({}))
    return values


def validate_select_filter_values(
    user_id: int,
    url: str,
    *,
    db_engine: Engine = default_engine,
) -> list[dict[str, Any]]:
    target_url = (url or "").strip()
    if not target_url:
        return []

    try:
        slug, query = parse_dashboard_url(target_url)
    except ValueError:
        return []

    workspace_root = user_workspace_root(user_id)
    dashboard_dir = workspace_root / "dashboard" / slug
    if not dashboard_dir.exists():
        return []

    try:
        dash = load_dashboard(dashboard_dir)
    except Exception:
        return []

    query_params = dict(parse_qsl(query, keep_blank_values=True))
    warnings: list[dict[str, Any]] = []
    for filter_def in dash.filters:
        if not isinstance(filter_def, SelectFilter):
            continue
        if not filter_def.options_query:
            continue
        value = query_params.get(filter_def.name)
        if value is None or value == "" or value == filter_def.default:
            continue
        allowed_options = execute_options_query(dash, filter_def, db_engine)
        allowed_values = {option_value for option_value, _ in allowed_options}
        if value in allowed_values:
            continue
        warnings.append(
            {
                "filter": filter_def.name,
                "value": value,
                "sample_allowed_values": [
                    option_value for option_value, _ in allowed_options[:5]
                ],
            }
        )
    return warnings


def _is_structure_error(message: str) -> bool:
    return message.startswith(STRUCTURE_ERROR_PREFIXES)


def _record_empty_issue(
    result: DashboardValidationResult, message: str, *, output: bool
) -> None:
    if result.unfiltered:
        if output:
            result.output_errors.append(message)
        else:
            result.query_errors.append(message)
        return
    result.warnings.append(message)


def _output_kind(value: Any) -> str:
    if isinstance(value, go.Figure):
        return "figure"
    if isinstance(value, pd.DataFrame):
        return "table"
    if isinstance(value, Metric):
        return "metric"
    return "scalar"


def _is_empty_scalar(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    return False


def _is_empty_output(value: Any) -> bool:
    if isinstance(value, go.Figure):
        return len(value.data) == 0
    if isinstance(value, pd.DataFrame):
        return value.empty or len(value.columns) == 0
    if isinstance(value, Metric):
        return _is_empty_scalar(value.value)
    return _is_empty_scalar(value)


def format_validation_result(result: DashboardValidationResult) -> str:
    return f"VALIDATION_RESULT {json.dumps(result.payload(), ensure_ascii=False)}"


def format_validation_summary(result: DashboardValidationResult) -> str:
    if result.pending:
        return f"Validation pending: {result.pending_reason}"
    warning_count = len(result.warnings)
    status = "warnings" if warning_count else "passed"
    return (
        f"Validation {status} "
        f"(queries={len(result.queries)}, outputs={len(result.outputs)}, warnings={warning_count})."
    )


def format_validation_error(result: DashboardValidationResult) -> str:
    lines = [
        f"Dashboard validation failed for {result.url} (unfiltered={str(result.unfiltered).lower()})."
    ]
    if result.query_errors:
        lines.append("Queries:")
        lines.extend(f"- {message}" for message in result.query_errors)
    if result.output_errors:
        lines.append("Outputs:")
        lines.extend(f"- {message}" for message in result.output_errors)
    if result.warnings:
        lines.append("Warnings:")
        lines.extend(f"- {message}" for message in result.warnings)
    return "\n".join(lines)


def validate_dashboard_url(
    user_id: int,
    url: str,
    *,
    db_engine: Engine = default_engine,
    strict_structure: bool = True,
) -> DashboardValidationResult:
    target_url = (url or "").strip()
    if not target_url:
        raise ValueError("url is required")

    slug, query = parse_dashboard_url(target_url)
    workspace_root = user_workspace_root(user_id)
    dashboard_dir = workspace_root / "dashboard" / slug
    if not dashboard_dir.exists():
        if strict_structure:
            raise ValueError(f"dashboard not found: {slug}")
        return DashboardValidationResult(
            url=f"/dashboard/{slug}",
            pending_reason=f"dashboard not found: {slug}",
        )

    try:
        dash = load_dashboard(dashboard_dir)
    except Exception as exc:
        message = str(exc)
        if not strict_structure and _is_structure_error(message):
            return DashboardValidationResult(
                url=f"/dashboard/{slug}",
                pending_reason=message,
            )
        raise

    filters = parse_dashboard_filters(dash, query)
    defaults = default_dashboard_filters(dash)
    result = DashboardValidationResult(
        url=target_url,
        unfiltered=(filters == defaults),
    )

    for query_name in sorted(dash.queries):
        sql = dash.queries[query_name]
        try:
            df = execute_query(sql, filters, db_engine)
        except Exception as exc:
            result.query_errors.append(f"{query_name}: {exc}")
            continue
        row_count = len(df)
        result.queries[query_name] = row_count
        if row_count == 0:
            _record_empty_issue(
                result,
                f"{query_name}: returned 0 rows",
                output=False,
            )

    clear_query_cache()
    for output_name in sorted(dash.outputs):
        try:
            output_value = execute_output(dash, output_name, filters, db_engine)
        except Exception as exc:
            result.output_errors.append(f"{output_name}: {exc}")
            continue
        kind = _output_kind(output_value)
        result.outputs[output_name] = kind
        if _is_empty_output(output_value):
            _record_empty_issue(
                result,
                f"{output_name}: returned empty {kind}",
                output=True,
            )

    return result


def validate_single_query(
    sql: str, *, db_engine: Engine = default_engine
) -> str | None:
    try:
        execute_query(sql, {}, db_engine)
    except Exception as exc:
        return str(exc)
    return None


def validate_outputs_syntax(source_code: str) -> str | None:
    try:
        compile(source_code, "outputs.py", "exec")
    except SyntaxError as exc:
        return f"SyntaxError: {exc}"
    return None


def validate_dashboard_structure(dashboard_dir: Path) -> list[str]:
    md_file = dashboard_dir / "dashboard.md"
    if not md_file.exists():
        return []

    try:
        ast = parse_dashboard_md(md_file.read_text())
    except Exception:
        return []

    component_names: set[str] = set()

    def walk(nodes):
        for node in nodes:
            if isinstance(node, ComponentNode):
                name = node.attrs.get("name")
                if name and node.type in ("fig", "df", "metric"):
                    component_names.add(name)
            if isinstance(node, ContainerNode):
                walk(node.children)

    walk(ast)

    outputs_file = dashboard_dir / "outputs.py"
    output_names: set[str] = set()
    if outputs_file.exists():
        try:
            output_names = set(load_outputs(outputs_file).keys())
        except Exception:
            pass

    queries_dir = dashboard_dir / "queries"
    query_names: set[str] = set()
    if queries_dir.exists():
        query_names = {f.stem for f in queries_dir.glob("*.sql")}

    warnings: list[str] = []

    missing = component_names - output_names
    if missing and output_names:
        for name in sorted(missing):
            warnings.append(f"dashboard.md references <{name}> but no @output function found")

    try:
        filters = extract_filters(ast)
    except Exception:
        return warnings

    for f in filters:
        if isinstance(f, SelectFilter) and f.options_query:
            if f.options_query not in query_names:
                warnings.append(
                    f"filter '{f.name}' references query '{f.options_query}' but no .sql file found"
                )

    return warnings
