"""dashboard.loader

Load dashboard folders and queries from queries/ folder.
"""

from __future__ import annotations

import importlib.util
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from varro.dashboard.models import get_outputs
from varro.dashboard.filters import Filter, validate_options_queries
from varro.dashboard.parser import ASTNode, parse_dashboard_md, extract_filters


@dataclass
class Dashboard:
    """A loaded dashboard."""

    name: str
    queries: dict[str, str]
    outputs: dict[str, Callable]
    ast: list[ASTNode]
    filters: list[Filter] = field(default_factory=list)


def load_queries(folder: Path) -> dict[str, str]:
    """Load queries from a queries/ folder.

    Each .sql file becomes a named query.
    Filename (without extension) is the query name.
    """
    queries_dir = folder / "queries"
    if not queries_dir.exists() or not queries_dir.is_dir():
        raise ValueError(f"Missing queries/ folder in {folder}")

    queries: dict[str, str] = {}
    for sql_file in queries_dir.glob("*.sql"):
        name = sql_file.stem
        queries[name] = sql_file.read_text().strip()

    if not queries:
        raise ValueError(f"No .sql files in {queries_dir}")

    return queries


def extract_params(query: str) -> set[str]:
    """Extract :param_name from a SQL query.

    Uses negative lookbehind to avoid matching PostgreSQL :: cast syntax.
    """
    return set(re.findall(r"(?<!:):(\w+)", query))


def load_dashboard(folder: Path) -> Dashboard:
    """Load a dashboard from a folder.

    Requires: queries/, outputs.py, dashboard.md
    """
    name = folder.name

    # Validate required files
    queries_dir = folder / "queries"
    outputs_file = folder / "outputs.py"
    md_file = folder / "dashboard.md"

    if not queries_dir.exists() or not queries_dir.is_dir():
        raise ValueError(f"Missing queries/ folder in {folder}")
    for f in [outputs_file, md_file]:
        if not f.exists():
            raise ValueError(f"Missing {f.name} in {folder}")

    # Load queries from folder
    queries = load_queries(folder)

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
    filters = extract_filters(ast)
    validate_options_queries(filters, queries)

    return Dashboard(
        name=name,
        queries=queries,
        outputs=outputs,
        ast=ast,
        filters=filters,
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

