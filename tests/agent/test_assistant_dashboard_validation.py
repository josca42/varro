from __future__ import annotations

import importlib
import json
from pathlib import Path
from types import SimpleNamespace

import pytest


@pytest.fixture
def assistant_module(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")

    import logfire

    monkeypatch.setattr(logfire, "configure", lambda **kwargs: None)
    monkeypatch.setattr(logfire, "instrument_pydantic_ai", lambda: None)

    utils = importlib.import_module("varro.agent.utils")
    monkeypatch.setattr(utils, "get_dim_tables", lambda: ())

    assistant = importlib.import_module("varro.agent.assistant")
    return importlib.reload(assistant)


# --- Write: per-file validation ---


def test_write_sql_file_validates_single_query(assistant_module, monkeypatch, tmp_path):
    slug_dir = tmp_path / "dashboard" / "sales" / "queries"
    slug_dir.mkdir(parents=True)
    sql_file = slug_dir / "q1.sql"
    sql_file.write_text("SELECT 1")

    monkeypatch.setattr(
        assistant_module,
        "write_file",
        lambda file_path, content, user_id: "Wrote 8 bytes to /dashboard/sales/queries/q1.sql.",
    )
    monkeypatch.setattr(
        assistant_module,
        "user_workspace_root",
        lambda user_id: tmp_path,
    )
    monkeypatch.setattr(
        assistant_module,
        "validate_single_query",
        lambda sql, **kw: None,
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    result = assistant_module.Write(ctx, "/dashboard/sales/queries/q1.sql", "SELECT 1")

    assert "SQL validation passed" in result


def test_write_sql_file_returns_error_as_string(assistant_module, monkeypatch, tmp_path):
    slug_dir = tmp_path / "dashboard" / "sales" / "queries"
    slug_dir.mkdir(parents=True)
    (slug_dir / "q1.sql").write_text("BAD SQL")

    monkeypatch.setattr(
        assistant_module,
        "write_file",
        lambda file_path, content, user_id: "Wrote 7 bytes to /dashboard/sales/queries/q1.sql.",
    )
    monkeypatch.setattr(
        assistant_module,
        "user_workspace_root",
        lambda user_id: tmp_path,
    )
    monkeypatch.setattr(
        assistant_module,
        "validate_single_query",
        lambda sql, **kw: "syntax error at position 0",
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    result = assistant_module.Write(ctx, "/dashboard/sales/queries/q1.sql", "BAD SQL")

    assert "SQL validation error" in result
    assert "syntax error" in result


def test_write_outputs_validates_syntax(assistant_module, monkeypatch, tmp_path):
    slug_dir = tmp_path / "dashboard" / "sales"
    slug_dir.mkdir(parents=True)
    (slug_dir / "outputs.py").write_text("x = 1")

    monkeypatch.setattr(
        assistant_module,
        "write_file",
        lambda file_path, content, user_id: "Wrote 5 bytes to /dashboard/sales/outputs.py.",
    )
    monkeypatch.setattr(
        assistant_module,
        "user_workspace_root",
        lambda user_id: tmp_path,
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    result = assistant_module.Write(ctx, "/dashboard/sales/outputs.py", "x = 1")

    assert "syntax OK" in result


def test_write_outputs_returns_syntax_error(assistant_module, monkeypatch, tmp_path):
    slug_dir = tmp_path / "dashboard" / "sales"
    slug_dir.mkdir(parents=True)
    (slug_dir / "outputs.py").write_text("def f(\n")

    monkeypatch.setattr(
        assistant_module,
        "write_file",
        lambda file_path, content, user_id: "Wrote 7 bytes to /dashboard/sales/outputs.py.",
    )
    monkeypatch.setattr(
        assistant_module,
        "user_workspace_root",
        lambda user_id: tmp_path,
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    result = assistant_module.Write(ctx, "/dashboard/sales/outputs.py", "def f(\n")

    assert "outputs.py validation error" in result
    assert "SyntaxError" in result


def test_write_dashboard_md_validates_structure(assistant_module, monkeypatch, tmp_path):
    slug_dir = tmp_path / "dashboard" / "sales"
    slug_dir.mkdir(parents=True)
    (slug_dir / "dashboard.md").write_text("# Test\n<fig name=\"chart\" />\n")

    monkeypatch.setattr(
        assistant_module,
        "write_file",
        lambda file_path, content, user_id: "Wrote 10 bytes to /dashboard/sales/dashboard.md.",
    )
    monkeypatch.setattr(
        assistant_module,
        "user_workspace_root",
        lambda user_id: tmp_path,
    )
    monkeypatch.setattr(
        assistant_module,
        "validate_dashboard_structure",
        lambda d: [],
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    result = assistant_module.Write(ctx, "/dashboard/sales/dashboard.md", "# Test")

    assert "structure OK" in result


def test_write_dashboard_md_returns_structure_warnings(assistant_module, monkeypatch, tmp_path):
    slug_dir = tmp_path / "dashboard" / "sales"
    slug_dir.mkdir(parents=True)
    (slug_dir / "dashboard.md").write_text("# Test")

    monkeypatch.setattr(
        assistant_module,
        "write_file",
        lambda file_path, content, user_id: "Wrote 10 bytes to /dashboard/sales/dashboard.md.",
    )
    monkeypatch.setattr(
        assistant_module,
        "user_workspace_root",
        lambda user_id: tmp_path,
    )
    monkeypatch.setattr(
        assistant_module,
        "validate_dashboard_structure",
        lambda d: ["dashboard.md references <chart> but no @output function found"],
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    result = assistant_module.Write(ctx, "/dashboard/sales/dashboard.md", "# Test")

    assert "structure warnings" in result
    assert "chart" in result


def test_write_non_dashboard_file_skips_validation(assistant_module, monkeypatch):
    monkeypatch.setattr(
        assistant_module,
        "write_file",
        lambda file_path, content, user_id: "Wrote 3 bytes to /notes.txt.",
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    result = assistant_module.Write(ctx, "/notes.txt", "abc")

    assert result == "Wrote 3 bytes to /notes.txt."


def test_write_never_raises_model_retry_for_validation_errors(
    assistant_module, monkeypatch, tmp_path
):
    """Write with validation errors should return a string, not raise ModelRetry."""
    slug_dir = tmp_path / "dashboard" / "sales" / "queries"
    slug_dir.mkdir(parents=True)
    (slug_dir / "q1.sql").write_text("BAD")

    monkeypatch.setattr(
        assistant_module,
        "write_file",
        lambda file_path, content, user_id: "Wrote 3 bytes to /dashboard/sales/queries/q1.sql.",
    )
    monkeypatch.setattr(
        assistant_module,
        "user_workspace_root",
        lambda user_id: tmp_path,
    )
    monkeypatch.setattr(
        assistant_module,
        "validate_single_query",
        lambda sql, **kw: "column does not exist",
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    # Should NOT raise ModelRetry
    result = assistant_module.Write(ctx, "/dashboard/sales/queries/q1.sql", "BAD")
    assert isinstance(result, str)
    assert "column does not exist" in result


# --- Edit: per-file validation ---


def test_edit_dashboard_query_validates_single_query(assistant_module, monkeypatch, tmp_path):
    slug_dir = tmp_path / "dashboard" / "sales" / "queries"
    slug_dir.mkdir(parents=True)
    (slug_dir / "q1.sql").write_text("SELECT 1")

    monkeypatch.setattr(
        assistant_module,
        "edit_file",
        lambda *args, **kwargs: "Replaced 1 occurrence(s) in /dashboard/sales/queries/q1.sql.",
    )
    monkeypatch.setattr(
        assistant_module,
        "user_workspace_root",
        lambda user_id: tmp_path,
    )
    monkeypatch.setattr(
        assistant_module,
        "validate_single_query",
        lambda sql, **kw: None,
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    result = assistant_module.Edit(ctx, "/dashboard/sales/queries/q1.sql", "old", "new")

    assert "SQL validation passed" in result


# --- ValidateDashboard tool (unchanged behavior) ---


def test_validate_dashboard_tool_returns_payload(assistant_module, monkeypatch):
    validation = importlib.import_module("varro.agent.dashboard_validation")
    result = validation.DashboardValidationResult(
        url="/dashboard/sales?region=North",
        unfiltered=False,
        queries={"q1": 0},
        outputs={"summary": "metric"},
        warnings=["q1: returned 0 rows"],
    )
    monkeypatch.setattr(
        assistant_module,
        "validate_dashboard_url",
        lambda user_id, url, strict_structure=True: result,
    )
    ctx = SimpleNamespace(
        deps=SimpleNamespace(user_id=7, request_current_url=lambda: "/dashboard/sales")
    )

    tool_result = assistant_module.ValidateDashboard(
        ctx, url="/dashboard/sales?region=North"
    )
    assert tool_result.startswith("VALIDATION_RESULT ")
    payload = json.loads(tool_result.removeprefix("VALIDATION_RESULT ").strip())
    assert payload["url"] == "/dashboard/sales?region=North"
    assert payload["warnings"] == ["q1: returned 0 rows"]


def test_validate_dashboard_tool_raises_model_retry_on_blocking_errors(
    assistant_module, monkeypatch
):
    validation = importlib.import_module("varro.agent.dashboard_validation")
    result = validation.DashboardValidationResult(
        url="/dashboard/sales",
        unfiltered=True,
        query_errors=["q1: returned 0 rows"],
    )
    monkeypatch.setattr(
        assistant_module,
        "validate_dashboard_url",
        lambda user_id, url, strict_structure=True: result,
    )
    ctx = SimpleNamespace(
        deps=SimpleNamespace(user_id=7, request_current_url=lambda: "/dashboard/sales")
    )

    with pytest.raises(assistant_module.ModelRetry) as exc:
        assistant_module.ValidateDashboard(ctx)
    assert "Dashboard validation failed" in str(exc.value)
