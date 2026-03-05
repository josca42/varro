from __future__ import annotations

import importlib
import resource
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


def test_worker_env_uses_writable_home_cache_paths():
    sandbox = importlib.import_module("varro.agent.sandbox")
    env = sandbox._worker_env()

    assert env["HOME"] == "/home/dev"
    assert env["XDG_CACHE_HOME"] == "/home/dev/.cache"
    assert env["XDG_CONFIG_HOME"] == "/home/dev/.config"
    assert env["MPLCONFIGDIR"] == "/home/dev/.cache/matplotlib"
    assert env["ARROW_NUM_THREADS"] == "1"
    assert env["OMP_NUM_THREADS"] == "1"


def test_int_setting_with_fallback_uses_primary_then_fallback(monkeypatch):
    sandbox = importlib.import_module("varro.agent.sandbox")

    class _Settings:
        def __init__(self, data):
            self.data = data

        def get(self, key):
            return self.data.get(key)

    monkeypatch.setattr(sandbox, "settings", _Settings({"A": "123", "B": "456"}))
    assert sandbox._int_setting_with_fallback("A", "B", 10) == 123

    monkeypatch.setattr(sandbox, "settings", _Settings({"B": "456"}))
    assert sandbox._int_setting_with_fallback("A", "B", 10) == 456

    monkeypatch.setattr(sandbox, "settings", _Settings({}))
    assert sandbox._int_setting_with_fallback("A", "B", 10) == 10


def test_default_limits_do_not_set_nproc():
    sandbox = importlib.import_module("varro.agent.sandbox")

    assert sandbox.BASH_LIMITS.nproc is None
    assert sandbox.WORKER_LIMITS.nproc is None


def test_apply_limits_skips_nproc_when_unset(monkeypatch):
    sandbox = importlib.import_module("varro.agent.sandbox")
    calls = []

    def fake_setrlimit(kind, values):
        calls.append((kind, values))

    monkeypatch.setattr(sandbox.resource, "setrlimit", fake_setrlimit)
    preexec = sandbox._apply_limits(
        sandbox.ResourceLimits(
            cpu_seconds=7,
            memory_bytes=11,
            nproc=None,
            nofile=13,
            fsize=17,
        )
    )

    preexec()

    kinds = {kind for kind, _ in calls}
    assert resource.RLIMIT_NPROC not in kinds
    assert resource.RLIMIT_CPU in kinds
    assert resource.RLIMIT_AS in kinds
    assert resource.RLIMIT_NOFILE in kinds
    assert resource.RLIMIT_FSIZE in kinds
