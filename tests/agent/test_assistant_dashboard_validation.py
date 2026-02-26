from __future__ import annotations

import importlib
import json
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


def test_write_dashboard_file_triggers_validation(assistant_module, monkeypatch):
    validation = importlib.import_module("varro.agent.dashboard_validation")
    result = validation.DashboardValidationResult(
        url="/dashboard/sales",
        unfiltered=True,
        queries={"q1": 3},
        outputs={"summary": "metric"},
    )
    monkeypatch.setattr(
        assistant_module,
        "write_file",
        lambda file_path, content, user_id: "Wrote 4 bytes to /dashboard/sales/outputs.py.",
    )
    monkeypatch.setattr(
        assistant_module,
        "validate_dashboard_url",
        lambda user_id, url, strict_structure=False: result,
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    tool_result = assistant_module.Write(ctx, "/dashboard/sales/outputs.py", "pass")

    assert tool_result.startswith("Wrote 4 bytes")
    assert "Validation passed" in tool_result
    assert tool_result.count("VALIDATION_RESULT ") == 1


def test_write_any_file_inside_dashboard_folder_triggers_validation(
    assistant_module, monkeypatch
):
    validation = importlib.import_module("varro.agent.dashboard_validation")
    result = validation.DashboardValidationResult(
        url="/dashboard/sales",
        unfiltered=True,
        queries={"q1": 3},
        outputs={"summary": "metric"},
    )
    calls = []
    monkeypatch.setattr(
        assistant_module,
        "write_file",
        lambda file_path, content, user_id: "Wrote 4 bytes to /dashboard/sales/note.txt.",
    )

    def _validate(user_id, url, strict_structure=False):
        calls.append((user_id, url, strict_structure))
        return result

    monkeypatch.setattr(assistant_module, "validate_dashboard_url", _validate)

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    tool_result = assistant_module.Write(ctx, "/dashboard/sales/note.txt", "pass")

    assert tool_result.startswith("Wrote 4 bytes")
    assert calls == [(1, "/dashboard/sales", False)]


def test_edit_dashboard_query_triggers_validation(assistant_module, monkeypatch):
    validation = importlib.import_module("varro.agent.dashboard_validation")
    result = validation.DashboardValidationResult(
        url="/dashboard/sales",
        unfiltered=True,
        queries={"q1": 2},
        outputs={"summary": "metric"},
    )
    monkeypatch.setattr(
        assistant_module,
        "edit_file",
        lambda *args, **kwargs: "Replaced 1 occurrence(s) in /dashboard/sales/queries/q1.sql.",
    )
    monkeypatch.setattr(
        assistant_module,
        "validate_dashboard_url",
        lambda user_id, url, strict_structure=False: result,
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    tool_result = assistant_module.Edit(
        ctx,
        "/dashboard/sales/queries/q1.sql",
        "old",
        "new",
    )

    assert tool_result.startswith("Replaced 1 occurrence")
    assert "VALIDATION_RESULT " in tool_result


def test_write_non_dashboard_file_skips_validation(assistant_module, monkeypatch):
    calls = {"count": 0}
    monkeypatch.setattr(
        assistant_module,
        "write_file",
        lambda file_path, content, user_id: "Wrote 3 bytes to /notes.txt.",
    )

    def _validate(*args, **kwargs):
        calls["count"] += 1
        raise AssertionError("should not be called")

    monkeypatch.setattr(assistant_module, "validate_dashboard_url", _validate)

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    tool_result = assistant_module.Write(ctx, "/notes.txt", "abc")

    assert tool_result == "Wrote 3 bytes to /notes.txt."
    assert calls["count"] == 0


def test_write_raises_model_retry_for_blocking_validation_errors(
    assistant_module, monkeypatch
):
    validation = importlib.import_module("varro.agent.dashboard_validation")
    result = validation.DashboardValidationResult(
        url="/dashboard/sales",
        unfiltered=True,
        queries={"q1": 0},
        outputs={"summary": "metric"},
        query_errors=["q1: returned 0 rows"],
    )
    monkeypatch.setattr(
        assistant_module,
        "write_file",
        lambda file_path, content, user_id: "Wrote 4 bytes to /dashboard/sales/outputs.py.",
    )
    monkeypatch.setattr(
        assistant_module,
        "validate_dashboard_url",
        lambda user_id, url, strict_structure=False: result,
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    with pytest.raises(assistant_module.ModelRetry) as exc:
        assistant_module.Write(ctx, "/dashboard/sales/outputs.py", "pass")
    assert "Dashboard validation failed" in str(exc.value)
    assert "Queries:" in str(exc.value)


def test_write_returns_warning_summary_without_blocking(assistant_module, monkeypatch):
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
        "write_file",
        lambda file_path, content, user_id: "Wrote 4 bytes to /dashboard/sales/outputs.py.",
    )
    monkeypatch.setattr(
        assistant_module,
        "validate_dashboard_url",
        lambda user_id, url, strict_structure=False: result,
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    tool_result = assistant_module.Write(ctx, "/dashboard/sales/outputs.py", "pass")

    assert "Validation warnings" in tool_result
    payload = json.loads(tool_result.split("VALIDATION_RESULT ", maxsplit=1)[1])
    assert payload["warnings"] == ["q1: returned 0 rows"]


def test_write_reports_validation_pending_for_incomplete_dashboard(
    assistant_module, monkeypatch
):
    validation = importlib.import_module("varro.agent.dashboard_validation")
    result = validation.DashboardValidationResult(
        url="/dashboard/sales",
        pending_reason="Missing outputs.py in /dashboard/sales",
    )
    monkeypatch.setattr(
        assistant_module,
        "write_file",
        lambda file_path, content, user_id: "Wrote 4 bytes to /dashboard/sales/dashboard.md.",
    )
    monkeypatch.setattr(
        assistant_module,
        "validate_dashboard_url",
        lambda user_id, url, strict_structure=False: result,
    )

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=1))
    tool_result = assistant_module.Write(ctx, "/dashboard/sales/dashboard.md", "pass")

    assert tool_result.startswith("Wrote 4 bytes")
    assert "Validation pending:" in tool_result
    assert "VALIDATION_RESULT " not in tool_result


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
