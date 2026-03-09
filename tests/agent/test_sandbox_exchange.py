from __future__ import annotations

import importlib


class _DummyProc:
    def __init__(self):
        self._alive = True
        self.stderr = iter(())
        self.stdin = None
        self.stdout = None

    def poll(self):
        return None if self._alive else 0

    def terminate(self):
        self._alive = False

    def wait(self, timeout=None):
        self._alive = False
        return 0

    def kill(self):
        self._alive = False


def test_exchange_dir_is_scoped_per_chat_and_cleaned_on_close(tmp_path, monkeypatch):
    sandbox = importlib.import_module("varro.agent.sandbox")
    user_root = tmp_path / "user" / "1"
    user_root.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(sandbox, "user_workspace_root", lambda user_id: user_root)
    monkeypatch.setattr(
        sandbox.SandboxShellProxy,
        "_spawn_worker",
        lambda self: _DummyProc(),
    )
    monkeypatch.setattr(
        sandbox.SandboxShellProxy,
        "_request",
        lambda self, payload: {"ok": True},
    )

    shell = sandbox.SandboxShellProxy(
        user_id=1,
        chat_id=5,
        snapshot_fp=tmp_path / "chat" / "1" / "5" / "shell.pkl",
    )

    assert shell._exchange_dir == user_root / ".varro_exchange" / "5"
    assert shell._exchange_dir.exists()

    shell.close(save_snapshot=False)

    assert not (user_root / ".varro_exchange" / "5").exists()


def test_exchange_dir_is_recreated_clean_when_chat_starts(tmp_path, monkeypatch):
    sandbox = importlib.import_module("varro.agent.sandbox")
    user_root = tmp_path / "user" / "1"
    stale_dir = user_root / ".varro_exchange" / "9"
    stale_dir.mkdir(parents=True, exist_ok=True)
    (stale_dir / "stale.bin").write_bytes(b"stale")

    monkeypatch.setattr(sandbox, "user_workspace_root", lambda user_id: user_root)
    monkeypatch.setattr(
        sandbox.SandboxShellProxy,
        "_spawn_worker",
        lambda self: _DummyProc(),
    )
    monkeypatch.setattr(
        sandbox.SandboxShellProxy,
        "_request",
        lambda self, payload: {"ok": True},
    )

    shell = sandbox.SandboxShellProxy(
        user_id=1,
        chat_id=9,
        snapshot_fp=tmp_path / "chat" / "1" / "9" / "shell.pkl",
    )
    try:
        assert shell._exchange_dir.exists()
        assert not (shell._exchange_dir / "stale.bin").exists()
    finally:
        shell.close(save_snapshot=False)


def test_worker_args_include_exchange_dir_argument(tmp_path):
    sandbox = importlib.import_module("varro.agent.sandbox")
    user_root = tmp_path / "user"
    snapshot_dir = tmp_path / "chat"
    args = sandbox._build_bwrap_worker_args(
        user_root,
        snapshot_dir,
        "/.varro_exchange/7",
    )

    idx = args.index("--exchange-dir")
    assert args[idx + 1] == "/.varro_exchange/7"
