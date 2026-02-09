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


def test_bash_returns_command_output_and_updates_cwd(assistant_module, monkeypatch):
    calls = []

    def fake_run_bash_command(user_id: int, cwd_rel: str, command: str):
        calls.append((user_id, cwd_rel, command))
        return "command output", "/next"

    monkeypatch.setattr(assistant_module, "run_bash_command", fake_run_bash_command)
    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=42, bash_cwd="/start"))

    output = assistant_module.Bash(ctx, command="ls /subjects")

    assert output == "command output"
    assert ctx.deps.bash_cwd == "/next"
    assert calls == [(42, "/start", "ls /subjects")]


def test_bash_uses_root_cwd_when_session_has_no_bash_cwd(assistant_module, monkeypatch):
    calls = []

    def fake_run_bash_command(user_id: int, cwd_rel: str, command: str):
        calls.append((user_id, cwd_rel, command))
        return "pwd output", "/"

    monkeypatch.setattr(assistant_module, "run_bash_command", fake_run_bash_command)
    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=9))

    output = assistant_module.Bash(ctx, command="pwd")

    assert output == "pwd output"
    assert ctx.deps.bash_cwd == "/"
    assert calls == [(9, "/", "pwd")]


def test_update_url_merges_params_and_updates_session_url(assistant_module):
    ctx = SimpleNamespace(deps=SimpleNamespace(current_url="/dashboard/sales?region=North"))

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
    assert ctx.deps.current_url == payload["url"]


def test_update_url_removes_params_with_none(assistant_module):
    ctx = SimpleNamespace(deps=SimpleNamespace(current_url="/dashboard/sales?region=North&period_to=2024-12-31"))

    output = assistant_module.UpdateUrl(
        ctx,
        params={"region": None, "period_to": ""},
    )

    payload = json.loads(output.removeprefix("UPDATE_URL ").strip())
    assert payload["url"] == "/dashboard/sales"
    assert payload["replace"] is False
    assert ctx.deps.current_url == "/dashboard/sales"
