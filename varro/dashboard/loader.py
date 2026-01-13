"""dashboard.loader

Load dashboard folders and parse queries.sql.
"""

from __future__ import annotations

import importlib.util
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from .models import get_outputs
from .parser import (
    ASTNode,
    ComponentNode,
    parse_dashboard_md,
    extract_filter_defs,
)


@dataclass
class Dashboard:
    """A loaded dashboard."""

    name: str
    queries: dict[str, str]
    outputs: dict[str, Callable]
    ast: list[ASTNode]
    filter_defs: list[ComponentNode] = field(default_factory=list)


def parse_queries(sql: str) -> dict[str, str]:
    """Parse queries.sql into named queries.

    Format:
        -- @query: query_name
        SELECT ...
    """
    queries: dict[str, str] = {}
    current: str | None = None
    lines: list[str] = []

    for line in sql.split("\n"):
        if match := re.match(r"--\s*@query:\s*(\w+)", line):
            if current:
                queries[current] = "\n".join(lines).strip()
            current = match.group(1)
            lines = []
        elif current is not None:
            lines.append(line)

    if current:
        queries[current] = "\n".join(lines).strip()

    return queries


def extract_params(query: str) -> set[str]:
    """Extract :param_name from a SQL query.

    Uses negative lookbehind to avoid matching PostgreSQL :: cast syntax.
    """
    return set(re.findall(r"(?<!:):(\w+)", query))


def load_dashboard(folder: Path) -> Dashboard:
    """Load a dashboard from a folder.

    Requires: queries.sql, outputs.py, dashboard.md
    """
    name = folder.name

    # Validate required files
    queries_file = folder / "queries.sql"
    outputs_file = folder / "outputs.py"
    md_file = folder / "dashboard.md"

    for f in [queries_file, outputs_file, md_file]:
        if not f.exists():
            raise ValueError(f"Missing {f.name} in {folder}")

    # Parse queries
    queries = parse_queries(queries_file.read_text())

    # Import outputs module
    spec = importlib.util.spec_from_file_location(
        f"dashboards.{name}.outputs", outputs_file
    )
    if spec is None or spec.loader is None:
        raise ValueError(f"Cannot load {outputs_file}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    outputs = get_outputs(module)

    # Parse markdown
    ast = parse_dashboard_md(md_file.read_text())
    filter_defs = extract_filter_defs(ast)

    return Dashboard(
        name=name,
        queries=queries,
        outputs=outputs,
        ast=ast,
        filter_defs=filter_defs,
    )


def load_dashboards(dashboards_dir: str | Path) -> dict[str, Dashboard]:
    """Load all dashboards from a directory."""
    dashboards: dict[str, Dashboard] = {}
    path = Path(dashboards_dir)

    if not path.exists():
        return dashboards

    for folder in path.iterdir():
        if folder.is_dir() and (folder / "dashboard.md").exists():
            dash = load_dashboard(folder)
            dashboards[dash.name] = dash

    return dashboards


__all__ = [
    "Dashboard",
    "parse_queries",
    "extract_params",
    "load_dashboard",
    "load_dashboards",
]
