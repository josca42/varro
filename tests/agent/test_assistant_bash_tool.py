from __future__ import annotations

import importlib
import json
from types import SimpleNamespace
from urllib.parse import parse_qs, urlparse

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


def test_bash_returns_command_output_and_persists_cwd(assistant_module, monkeypatch):
    calls = []

    def fake_load_bash_cwd(user_id: int, chat_id: int) -> str:
        calls.append(("load", user_id, chat_id))
        return "/start"

    def fake_run_bash_command(user_id: int, cwd_rel: str, command: str):
        calls.append(("run", user_id, cwd_rel, command))
        return "command output", "/next"

    def fake_save_bash_cwd(user_id: int, chat_id: int, cwd: str) -> None:
        calls.append(("save", user_id, chat_id, cwd))

    monkeypatch.setattr(assistant_module, "load_bash_cwd", fake_load_bash_cwd)
    monkeypatch.setattr(assistant_module, "run_bash_command", fake_run_bash_command)
    monkeypatch.setattr(assistant_module, "save_bash_cwd", fake_save_bash_cwd)

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=42, chat_id=7))
    output = assistant_module.Bash(ctx, command="ls /subjects")

    assert output == "command output\n[cwd=/next]"
    assert calls == [
        ("load", 42, 7),
        ("run", 42, "/start", "ls /subjects"),
        ("save", 42, 7, "/next"),
    ]


def test_bash_uses_loaded_root_cwd_when_store_returns_root(assistant_module, monkeypatch):
    calls = []

    def fake_load_bash_cwd(user_id: int, chat_id: int) -> str:
        calls.append(("load", user_id, chat_id))
        return "/"

    def fake_run_bash_command(user_id: int, cwd_rel: str, command: str):
        calls.append(("run", user_id, cwd_rel, command))
        return "pwd output", "/"

    def fake_save_bash_cwd(user_id: int, chat_id: int, cwd: str) -> None:
        calls.append(("save", user_id, chat_id, cwd))

    monkeypatch.setattr(assistant_module, "load_bash_cwd", fake_load_bash_cwd)
    monkeypatch.setattr(assistant_module, "run_bash_command", fake_run_bash_command)
    monkeypatch.setattr(assistant_module, "save_bash_cwd", fake_save_bash_cwd)

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=9, chat_id=2))
    output = assistant_module.Bash(ctx, command="pwd")

    assert output == "pwd output\n[cwd=/]"
    assert calls == [
        ("load", 9, 2),
        ("run", 9, "/", "pwd"),
        ("save", 9, 2, "/"),
    ]


def test_update_url_merges_params_using_request_current_url(assistant_module):
    ctx = SimpleNamespace(
        deps=SimpleNamespace(
            user_id=7,
            request_current_url=lambda: "/dashboard/sales?region=North"
        )
    )

    output = assistant_module.UpdateUrl(
        ctx,
        params={"region": "South", "period_from": "2024-01-01"},
        replace=True,
    )

    assert output.startswith("UPDATE_URL ")
    payload = json.loads(output.removeprefix("UPDATE_URL ").strip())
    parsed = urlparse(payload["url"])
    assert parsed.path == "/dashboard/sales"
    assert parse_qs(parsed.query) == {
        "region": ["South"],
        "period_from": ["2024-01-01"],
    }
    assert payload["replace"] is True


def test_update_url_removes_params_with_none(assistant_module):
    ctx = SimpleNamespace(
        deps=SimpleNamespace(
            user_id=7,
            request_current_url=lambda: "/dashboard/sales?region=North&period_to=2024-12-31"
        )
    )

    output = assistant_module.UpdateUrl(
        ctx,
        params={"region": None, "period_to": ""},
    )

    payload = json.loads(output.removeprefix("UPDATE_URL ").strip())
    assert payload["url"] == "/dashboard/sales"
    assert payload["replace"] is False


def test_update_url_updates_current_url_when_setter_available(assistant_module):
    state = {"url": "/dashboard/sales?region=North"}
    ctx = SimpleNamespace(
        deps=SimpleNamespace(
            user_id=7,
            request_current_url=lambda: state["url"],
            request_set_current_url=lambda url: state.__setitem__("url", url),
        )
    )

    output = assistant_module.UpdateUrl(ctx, params={"region": "South"})

    payload = json.loads(output.removeprefix("UPDATE_URL ").strip())
    assert payload["url"] == "/dashboard/sales?region=South"
    assert state["url"] == "/dashboard/sales?region=South"


def test_update_url_includes_filter_warnings_when_value_is_invalid(
    assistant_module, monkeypatch
):
    monkeypatch.setattr(
        assistant_module,
        "validate_select_filter_values",
        lambda user_id, url: [
            {
                "filter": "region",
                "value": "Region Hovedstaden",
                "sample_allowed_values": ["84", "85"],
            }
        ],
    )
    ctx = SimpleNamespace(
        deps=SimpleNamespace(
            user_id=7,
            request_current_url=lambda: "/dashboard/befolkning",
        )
    )

    output = assistant_module.UpdateUrl(
        ctx,
        params={"region": "Region Hovedstaden"},
    )

    payload = json.loads(output.removeprefix("UPDATE_URL ").strip())
    assert payload["url"] == "/dashboard/befolkning?region=Region+Hovedstaden"
    assert payload["warnings"] == [
        {
            "filter": "region",
            "value": "Region Hovedstaden",
            "sample_allowed_values": ["84", "85"],
        }
    ]
