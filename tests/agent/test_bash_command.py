from __future__ import annotations

import importlib
from pathlib import Path
from types import SimpleNamespace


def test_run_bash_command_delegates_to_vanilla_in_dev_mode(monkeypatch):
    sandbox = importlib.import_module("varro.agent.sandbox")
    monkeypatch.setattr(sandbox, "SHELL_MODE", "DEV")
    monkeypatch.setattr(
        sandbox,
        "run_bash_command_vanilla",
        lambda user_id, cwd_rel, command: ("ok", "/next"),
    )

    output, cwd = sandbox.run_bash_command(1, "/", "pwd")

    assert output == "ok"
    assert cwd == "/next"


def test_run_bash_command_blocks_delete_targets_in_readonly_roots(tmp_path: Path, monkeypatch):
    sandbox = importlib.import_module("varro.agent.sandbox")
    monkeypatch.setattr(sandbox, "SHELL_MODE", "BWRAP")
    monkeypatch.setattr(sandbox, "user_workspace_root", lambda user_id: tmp_path)
    monkeypatch.setattr(
        sandbox,
        "extract_commands",
        lambda command: ([["rm", "-rf", "/subjects"]], None, None),
    )

    called = {"run": False}

    def fake_run(*args, **kwargs):
        called["run"] = True
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr(sandbox.subprocess, "run", fake_run)

    output, cwd = sandbox.run_bash_command(1, "/", "rm -rf /subjects")

    assert output == "Error: path is read-only"
    assert cwd == "/"
    assert called["run"] is False


def test_run_bash_command_allows_delete_outside_readonly_roots(tmp_path: Path, monkeypatch):
    sandbox = importlib.import_module("varro.agent.sandbox")
    monkeypatch.setattr(sandbox, "SHELL_MODE", "BWRAP")
    monkeypatch.setattr(sandbox, "user_workspace_root", lambda user_id: tmp_path)
    monkeypatch.setattr(
        sandbox,
        "extract_commands",
        lambda command: ([["rm", "-rf", "/dashboard/tmp.txt"]], None, None),
    )

    called = {"run": False}

    def fake_run(*args, **kwargs):
        called["run"] = True
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr(sandbox.subprocess, "run", fake_run)

    output, cwd = sandbox.run_bash_command(1, "/", "rm -rf /dashboard/tmp.txt")

    assert output == ""
    assert cwd == "/"
    assert called["run"] is True


def test_run_bash_command_blocks_disallowed_commands(tmp_path: Path, monkeypatch):
    sandbox = importlib.import_module("varro.agent.sandbox")
    monkeypatch.setattr(sandbox, "SHELL_MODE", "BWRAP")
    monkeypatch.setattr(sandbox, "user_workspace_root", lambda user_id: tmp_path)

    output, cwd = sandbox.run_bash_command(1, "/", "python -c 'print(1)'")

    assert output == "Error: command not allowed: python"
    assert cwd == "/"
