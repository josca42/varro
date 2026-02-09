from __future__ import annotations

import importlib
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
