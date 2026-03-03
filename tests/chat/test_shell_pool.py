from __future__ import annotations

import asyncio
from datetime import timedelta

import dill
import varro.chat.shell_pool as shell_pool_mod


class _DummyHistoryManager:
    def __init__(self):
        self.ended = False

    def end_session(self):
        self.ended = True


class _DummyShell:
    def __init__(self):
        self.user_ns = {}
        self.history_manager = _DummyHistoryManager()
        self.reset_calls: list[bool] = []
        self.run_cells: list[str] = []

    def run_cell(self, code: str):
        self.run_cells.append(code)

    def reset(self, new_session: bool):
        self.reset_calls.append(new_session)
        self.user_ns = {}


def test_shell_pool_lease_loads_snapshot_when_entry_missing(tmp_path, monkeypatch):
    async def scenario():
        monkeypatch.setattr(shell_pool_mod, "DATA_DIR", tmp_path)
        first_shell = _DummyShell()
        restored_shell = _DummyShell()
        created = [first_shell, restored_shell]

        def fake_create_shell(*, user_id: int, chat_id: int, snapshot_fp):
            shell = created.pop(0)
            if snapshot_fp.exists():
                with snapshot_fp.open("rb") as f:
                    loaded = dill.load(f)
                if isinstance(loaded, dict):
                    shell.user_ns.update(loaded)
            return shell

        def fake_close_shell(shell, *, save_snapshot: bool, snapshot_fp):
            if save_snapshot:
                snapshot_fp.parent.mkdir(parents=True, exist_ok=True)
                with snapshot_fp.open("wb") as f:
                    dill.dump(getattr(shell, "user_ns", {}), f)

        monkeypatch.setattr(shell_pool_mod, "create_shell", fake_create_shell)
        monkeypatch.setattr(shell_pool_mod, "close_shell", fake_close_shell)

        pool = shell_pool_mod.ShellPool(ttl=timedelta(minutes=10), cleanup_interval=60)

        async with pool.lease(user_id=2, chat_id=5) as shell:
            shell.user_ns["answer"] = 42

        pool._entries[(2, 5)].last_active -= timedelta(minutes=1)
        await pool.evict_idle(ttl=timedelta(seconds=0))

        assert shell_pool_mod.shell_snapshot_fp(2, 5).exists()

        next_pool = shell_pool_mod.ShellPool(ttl=timedelta(minutes=10), cleanup_interval=60)
        async with next_pool.lease(user_id=2, chat_id=5):
            pass

        assert restored_shell.user_ns["answer"] == 42

    asyncio.run(scenario())


def test_shell_pool_remove_chat_evicts_entry_and_snapshot(tmp_path, monkeypatch):
    async def scenario():
        monkeypatch.setattr(shell_pool_mod, "DATA_DIR", tmp_path)
        shell = _DummyShell()
        monkeypatch.setattr(
            shell_pool_mod,
            "create_shell",
            lambda *, user_id, chat_id, snapshot_fp: shell,
        )

        def fake_close_shell(shell, *, save_snapshot: bool, snapshot_fp):
            if save_snapshot:
                snapshot_fp.parent.mkdir(parents=True, exist_ok=True)
                with snapshot_fp.open("wb") as f:
                    dill.dump(getattr(shell, "user_ns", {}), f)

        monkeypatch.setattr(shell_pool_mod, "close_shell", fake_close_shell)

        pool = shell_pool_mod.ShellPool(ttl=timedelta(minutes=10), cleanup_interval=60)
        async with pool.lease(user_id=1, chat_id=8) as leased:
            leased.user_ns["x"] = 1

        pool._entries[(1, 8)].last_active -= timedelta(minutes=1)
        await pool.evict_idle(ttl=timedelta(seconds=0))

        snapshot_fp = shell_pool_mod.shell_snapshot_fp(1, 8)
        assert snapshot_fp.exists()

        async with pool.lease(user_id=1, chat_id=8):
            pass
        assert (1, 8) in pool._entries

        await pool.remove_chat(1, 8)

        assert (1, 8) not in pool._entries
        assert not snapshot_fp.exists()

    asyncio.run(scenario())
