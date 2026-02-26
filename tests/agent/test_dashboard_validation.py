from __future__ import annotations

import importlib
from pathlib import Path
from types import SimpleNamespace

import pandas as pd
import plotly.graph_objects as go

from varro.dashboard.filters import SelectFilter
from varro.dashboard.models import Metric


def _workspace_root(tmp_path: Path, slug: str = "sales") -> Path:
    root = tmp_path / "user" / "1"
    (root / "dashboard" / slug).mkdir(parents=True)
    return root


def _dashboard(outputs: dict[str, object]) -> SimpleNamespace:
    return SimpleNamespace(
        filters=[SelectFilter(type="select", name="region", default="all")],
        queries={"q1": "select 1"},
        outputs=outputs,
    )


def test_validate_unfiltered_empty_query_is_blocking(tmp_path: Path, monkeypatch) -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    root = _workspace_root(tmp_path)
    dash = _dashboard({"summary": object()})

    monkeypatch.setattr(validation, "user_workspace_root", lambda user_id: root)
    monkeypatch.setattr(validation, "load_dashboard", lambda folder: dash)
    monkeypatch.setattr(
        validation,
        "execute_query",
        lambda query, filters, engine: pd.DataFrame(columns=["value"]),
    )
    monkeypatch.setattr(
        validation,
        "execute_output",
        lambda dash, output_name, filters, engine: Metric(value=1, label="ok"),
    )

    result = validation.validate_dashboard_url(
        1,
        "/dashboard/sales",
        db_engine=None,
        strict_structure=True,
    )

    assert result.unfiltered is True
    assert result.has_errors
    assert any("returned 0 rows" in message for message in result.query_errors)
    assert not result.warnings


def test_validate_filtered_empty_query_is_warning(tmp_path: Path, monkeypatch) -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    root = _workspace_root(tmp_path)
    dash = _dashboard({"summary": object()})

    monkeypatch.setattr(validation, "user_workspace_root", lambda user_id: root)
    monkeypatch.setattr(validation, "load_dashboard", lambda folder: dash)
    monkeypatch.setattr(
        validation,
        "execute_query",
        lambda query, filters, engine: pd.DataFrame(columns=["value"]),
    )
    monkeypatch.setattr(
        validation,
        "execute_output",
        lambda dash, output_name, filters, engine: Metric(value=1, label="ok"),
    )

    result = validation.validate_dashboard_url(
        1,
        "/dashboard/sales?region=North",
        db_engine=None,
        strict_structure=True,
    )

    assert result.unfiltered is False
    assert not result.has_errors
    assert any("returned 0 rows" in message for message in result.warnings)


def test_validate_output_runtime_exception_is_blocking(tmp_path: Path, monkeypatch) -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    root = _workspace_root(tmp_path)
    dash = _dashboard({"broken": object()})

    monkeypatch.setattr(validation, "user_workspace_root", lambda user_id: root)
    monkeypatch.setattr(validation, "load_dashboard", lambda folder: dash)
    monkeypatch.setattr(
        validation,
        "execute_query",
        lambda query, filters, engine: pd.DataFrame({"value": [1]}),
    )

    def _raise_output(*args, **kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(validation, "execute_output", _raise_output)

    result = validation.validate_dashboard_url(
        1,
        "/dashboard/sales",
        db_engine=None,
        strict_structure=True,
    )

    assert result.has_errors
    assert any("boom" in message for message in result.output_errors)


def test_validate_unfiltered_empty_figure_and_table_are_blocking(
    tmp_path: Path, monkeypatch
) -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    root = _workspace_root(tmp_path)
    dash = _dashboard({"fig": object(), "tbl": object()})

    monkeypatch.setattr(validation, "user_workspace_root", lambda user_id: root)
    monkeypatch.setattr(validation, "load_dashboard", lambda folder: dash)
    monkeypatch.setattr(
        validation,
        "execute_query",
        lambda query, filters, engine: pd.DataFrame({"value": [1]}),
    )

    def _output_value(dash, output_name, filters, engine):
        if output_name == "fig":
            return go.Figure()
        return pd.DataFrame()

    monkeypatch.setattr(validation, "execute_output", _output_value)

    result = validation.validate_dashboard_url(
        1,
        "/dashboard/sales",
        db_engine=None,
        strict_structure=True,
    )

    assert result.has_errors
    assert any("fig: returned empty figure" == message for message in result.output_errors)
    assert any("tbl: returned empty table" == message for message in result.output_errors)


def test_validate_filtered_empty_figure_and_table_are_warnings(
    tmp_path: Path, monkeypatch
) -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    root = _workspace_root(tmp_path)
    dash = _dashboard({"fig": object(), "tbl": object()})

    monkeypatch.setattr(validation, "user_workspace_root", lambda user_id: root)
    monkeypatch.setattr(validation, "load_dashboard", lambda folder: dash)
    monkeypatch.setattr(
        validation,
        "execute_query",
        lambda query, filters, engine: pd.DataFrame({"value": [1]}),
    )

    def _output_value(dash, output_name, filters, engine):
        if output_name == "fig":
            return go.Figure()
        return pd.DataFrame()

    monkeypatch.setattr(validation, "execute_output", _output_value)

    result = validation.validate_dashboard_url(
        1,
        "/dashboard/sales?region=North",
        db_engine=None,
        strict_structure=True,
    )

    assert not result.has_errors
    assert "fig: returned empty figure" in result.warnings
    assert "tbl: returned empty table" in result.warnings


def test_validate_unfiltered_none_and_blank_scalar_are_blocking(
    tmp_path: Path, monkeypatch
) -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    root = _workspace_root(tmp_path)
    dash = _dashboard({"none_value": object(), "blank_value": object()})

    monkeypatch.setattr(validation, "user_workspace_root", lambda user_id: root)
    monkeypatch.setattr(validation, "load_dashboard", lambda folder: dash)
    monkeypatch.setattr(
        validation,
        "execute_query",
        lambda query, filters, engine: pd.DataFrame({"value": [1]}),
    )

    def _output_value(dash, output_name, filters, engine):
        if output_name == "none_value":
            return None
        return "   "

    monkeypatch.setattr(validation, "execute_output", _output_value)

    result = validation.validate_dashboard_url(
        1,
        "/dashboard/sales",
        db_engine=None,
        strict_structure=True,
    )

    assert result.has_errors
    assert "none_value: returned empty scalar" in result.output_errors
    assert "blank_value: returned empty scalar" in result.output_errors


def test_validate_unfiltered_zero_and_false_scalar_are_valid(
    tmp_path: Path, monkeypatch
) -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    root = _workspace_root(tmp_path)
    dash = _dashboard({"zero_value": object(), "false_value": object()})

    monkeypatch.setattr(validation, "user_workspace_root", lambda user_id: root)
    monkeypatch.setattr(validation, "load_dashboard", lambda folder: dash)
    monkeypatch.setattr(
        validation,
        "execute_query",
        lambda query, filters, engine: pd.DataFrame({"value": [1]}),
    )

    def _output_value(dash, output_name, filters, engine):
        if output_name == "zero_value":
            return 0
        return False

    monkeypatch.setattr(validation, "execute_output", _output_value)

    result = validation.validate_dashboard_url(
        1,
        "/dashboard/sales",
        db_engine=None,
        strict_structure=True,
    )

    assert not result.has_errors
    assert not result.warnings


def test_validate_with_incomplete_structure_returns_pending_when_not_strict(
    tmp_path: Path, monkeypatch
) -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    root = _workspace_root(tmp_path)

    monkeypatch.setattr(validation, "user_workspace_root", lambda user_id: root)

    def _raise_missing(folder):
        raise ValueError(f"Missing outputs.py in {folder}")

    monkeypatch.setattr(validation, "load_dashboard", _raise_missing)

    result = validation.validate_dashboard_url(
        1,
        "/dashboard/sales",
        db_engine=None,
        strict_structure=False,
    )

    assert result.pending
    assert result.pending_reason is not None
    assert not result.has_errors


# --- Per-file validation functions ---


def test_validate_outputs_syntax_ok() -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    assert validation.validate_outputs_syntax("x = 1\ndef f(): pass") is None


def test_validate_outputs_syntax_error() -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    result = validation.validate_outputs_syntax("def f(\n")
    assert result is not None
    assert "SyntaxError" in result


def test_validate_dashboard_structure_missing_output_ref(tmp_path: Path) -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    dashboard_dir = tmp_path / "myboard"
    dashboard_dir.mkdir()
    (dashboard_dir / "dashboard.md").write_text(
        '# Test\n<fig name="chart" />\n<metric name="total" />\n'
    )
    (dashboard_dir / "outputs.py").write_text(
        "from varro.dashboard.models import output, Metric\n"
        "@output\ndef total(): return Metric(value=1, label='x')\n"
    )

    warnings = validation.validate_dashboard_structure(dashboard_dir)
    assert any("chart" in w for w in warnings)
    assert not any("total" in w for w in warnings)


def test_validate_dashboard_structure_missing_options_query(tmp_path: Path) -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    dashboard_dir = tmp_path / "myboard"
    dashboard_dir.mkdir()
    queries_dir = dashboard_dir / "queries"
    queries_dir.mkdir()
    (queries_dir / "data.sql").write_text("SELECT 1")
    (dashboard_dir / "dashboard.md").write_text(
        '::: filters\n<filter-select name="region" options="query:regions" default="all" />\n:::\n'
    )

    warnings = validation.validate_dashboard_structure(dashboard_dir)
    assert any("regions" in w and "no .sql file found" in w for w in warnings)


def test_validate_dashboard_structure_all_ok(tmp_path: Path) -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    dashboard_dir = tmp_path / "myboard"
    dashboard_dir.mkdir()
    queries_dir = dashboard_dir / "queries"
    queries_dir.mkdir()
    (queries_dir / "regions.sql").write_text("SELECT 1")
    (dashboard_dir / "outputs.py").write_text(
        "from varro.dashboard.models import output, Metric\n"
        "@output\ndef total(): return Metric(value=1, label='x')\n"
    )
    (dashboard_dir / "dashboard.md").write_text(
        '::: filters\n<filter-select name="region" options="query:regions" default="all" />\n:::\n'
        '<metric name="total" />\n'
    )

    warnings = validation.validate_dashboard_structure(dashboard_dir)
    assert warnings == []


def test_validate_select_filter_values_warns_on_invalid_select_value(
    tmp_path: Path, monkeypatch
) -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    root = _workspace_root(tmp_path)
    dash = SimpleNamespace(
        filters=[
            SelectFilter(
                type="select",
                name="region",
                default="all",
                options_query="regions",
            )
        ],
        queries={"regions": "select 1"},
        outputs={},
    )

    monkeypatch.setattr(validation, "user_workspace_root", lambda user_id: root)
    monkeypatch.setattr(validation, "load_dashboard", lambda folder: dash)
    monkeypatch.setattr(
        validation,
        "execute_options_query",
        lambda dash, filter_def, engine: [
            ("84", "Region Hovedstaden"),
            ("85", "Region Sjælland"),
        ],
    )

    warnings = validation.validate_select_filter_values(
        1,
        "/dashboard/sales?region=Region+Hovedstaden",
        db_engine=None,
    )
    assert warnings == [
        {
            "filter": "region",
            "value": "Region Hovedstaden",
            "sample_allowed_values": ["84", "85"],
        }
    ]


def test_validate_select_filter_values_accepts_valid_select_value(
    tmp_path: Path, monkeypatch
) -> None:
    validation = importlib.import_module("varro.agent.dashboard_validation")
    root = _workspace_root(tmp_path)
    dash = SimpleNamespace(
        filters=[
            SelectFilter(
                type="select",
                name="region",
                default="all",
                options_query="regions",
            )
        ],
        queries={"regions": "select 1"},
        outputs={},
    )

    monkeypatch.setattr(validation, "user_workspace_root", lambda user_id: root)
    monkeypatch.setattr(validation, "load_dashboard", lambda folder: dash)
    monkeypatch.setattr(
        validation,
        "execute_options_query",
        lambda dash, filter_def, engine: [
            ("84", "Region Hovedstaden"),
            ("85", "Region Sjælland"),
        ],
    )

    warnings = validation.validate_select_filter_values(
        1,
        "/dashboard/sales?region=84",
        db_engine=None,
    )
    assert warnings == []
