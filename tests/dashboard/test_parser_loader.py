from __future__ import annotations

from pathlib import Path

import pytest

from varro.dashboard.loader import load_dashboard
from varro.dashboard.parser import ContainerNode, extract_filters, parse_dashboard_md


def test_parse_example_dashboard_builds_expected_structure() -> None:
    content = Path("example_dashboard_folder/sales/dashboard.md").read_text()
    ast = parse_dashboard_md(content)

    top_level_containers = [n for n in ast if isinstance(n, ContainerNode)]
    types = [node.type for node in top_level_containers]
    assert types == ["filters", "grid", "tabs"]

    filters = extract_filters(ast)
    assert [f.name for f in filters] == ["region", "period"]

    tabs = next(node for node in top_level_containers if node.type == "tabs")
    tab_names = [
        child.attrs.get("name")
        for child in tabs.children
        if isinstance(child, ContainerNode) and child.type == "tab"
    ]
    assert tab_names == ["Trend", "Regions", "Age Groups"]


def test_load_dashboard_reads_queries_outputs_and_filters(dashboard_env) -> None:
    dash = load_dashboard(dashboard_env.dashboard_path)

    assert set(dash.queries) == {"regions", "population_trend", "population_by_region"}
    assert set(dash.outputs) == {
        "total_population",
        "periods_shown",
        "population_trend_chart",
        "region_table",
    }
    assert [f.name for f in dash.filters] == ["region", "period", "include_estimate"]


def test_load_dashboard_requires_all_files(tmp_path: Path) -> None:
    folder = tmp_path / "broken"
    folder.mkdir()
    (folder / "queries").mkdir()
    (folder / "queries" / "q.sql").write_text("SELECT 1")
    (folder / "dashboard.md").write_text("# Missing outputs")

    with pytest.raises(ValueError, match="Missing outputs.py"):
        load_dashboard(folder)
