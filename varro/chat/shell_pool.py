from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

import dill

from varro.agent.ipython_shell import JUPYTER_INITIAL_IMPORTS, TerminalInteractiveShell, get_shell
from varro.config import DATA_DIR


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def shell_snapshot_fp(user_id: int, chat_id: int) -> Path:
    return DATA_DIR / "chat" / str(user_id) / str(chat_id) / "shell.pkl"


@dataclass
class ShellEntry:
    shell: TerminalInteractiveShell
    lock: asyncio.Lock = field(default_factory=asyncio.Lock)
    in_use_count: int = 0
    last_active: datetime = field(default_factory=_utc_now)


class ShellPool:
    def __init__(
        self,
        *,
        ttl: timedelta = timedelta(minutes=10),
        cleanup_interval: int = 60,
    ):
        self._ttl = ttl
        self._cleanup_interval = cleanup_interval
        self._entries: dict[tuple[int, int], ShellEntry] = {}
        self._lock = asyncio.Lock()
        self._cleanup_task: asyncio.Task | None = None

    @asynccontextmanager
    async def lease(self, *, user_id: int, chat_id: int):
        key = (user_id, chat_id)
        entry = await self._acquire(key, user_id=user_id, chat_id=chat_id)
        try:
            yield entry.shell
        finally:
            await self._release(key)

    async def invalidate(self, user_id: int, chat_id: int) -> None:
        async with self._lock:
            entry = self._entries.pop((user_id, chat_id), None)
        if entry is None:
            return
        self._close_shell(entry.shell, save_snapshot=False, user_id=user_id, chat_id=chat_id)

    async def remove_chat(self, user_id: int, chat_id: int) -> None:
        async with self._lock:
            entry = self._entries.pop((user_id, chat_id), None)
        if entry is not None:
            self._close_shell(entry.shell, save_snapshot=False, user_id=user_id, chat_id=chat_id)
        shell_snapshot_fp(user_id, chat_id).unlink(missing_ok=True)

    async def evict_idle(self, ttl: timedelta | None = None) -> None:
        idle_ttl = self._ttl if ttl is None else ttl
        now = _utc_now()
        evicted: list[tuple[tuple[int, int], ShellEntry]] = []

        async with self._lock:
            for key, entry in list(self._entries.items()):
                if entry.in_use_count != 0:
                    continue
                if now - entry.last_active <= idle_ttl:
                    continue
                self._entries.pop(key, None)
                evicted.append((key, entry))

        for (user_id, chat_id), entry in evicted:
            self._close_shell(entry.shell, save_snapshot=True, user_id=user_id, chat_id=chat_id)

    def start_cleanup_task(
        self,
        *,
        ttl: timedelta | None = None,
        interval: int | None = None,
    ) -> None:
        if self._cleanup_task and not self._cleanup_task.done():
            return

        idle_ttl = self._ttl if ttl is None else ttl
        delay = self._cleanup_interval if interval is None else interval

        async def _loop() -> None:
            while True:
                await asyncio.sleep(delay)
                await self.evict_idle(idle_ttl)

        self._cleanup_task = asyncio.create_task(_loop())

    def stop_cleanup_task(self) -> None:
        if self._cleanup_task and not self._cleanup_task.done():
            self._cleanup_task.cancel()

    async def _acquire(self, key: tuple[int, int], *, user_id: int, chat_id: int) -> ShellEntry:
        async with self._lock:
            entry = self._entries.get(key)
            if entry is None:
                shell = get_shell()
                shell.run_cell(JUPYTER_INITIAL_IMPORTS)
                self._load_snapshot(shell, user_id=user_id, chat_id=chat_id)
                entry = ShellEntry(shell=shell)
                self._entries[key] = entry

            entry.in_use_count += 1
            entry.last_active = _utc_now()
            return entry

    async def _release(self, key: tuple[int, int]) -> None:
        async with self._lock:
            entry = self._entries.get(key)
            if entry is None:
                return
            entry.in_use_count = max(0, entry.in_use_count - 1)
            entry.last_active = _utc_now()

    def _close_shell(
        self,
        shell: TerminalInteractiveShell,
        *,
        save_snapshot: bool,
        user_id: int,
        chat_id: int,
    ) -> None:
        if save_snapshot:
            self._save_snapshot(shell, user_id=user_id, chat_id=chat_id)
        try:
            shell.reset(new_session=False)
            if shell.history_manager:
                shell.history_manager.end_session()
        except Exception:
            return

    def _save_snapshot(self, shell: TerminalInteractiveShell, *, user_id: int, chat_id: int) -> None:
        fp = shell_snapshot_fp(user_id, chat_id)
        fp.parent.mkdir(parents=True, exist_ok=True)
        try:
            with fp.open("wb") as f:
                dill.dump(getattr(shell, "user_ns", {}), f)
        except Exception:
            fp.unlink(missing_ok=True)

    def _load_snapshot(self, shell: TerminalInteractiveShell, *, user_id: int, chat_id: int) -> None:
        fp = shell_snapshot_fp(user_id, chat_id)
        if not fp.exists():
            return
        with fp.open("rb") as f:
            value = dill.load(f)
        if isinstance(value, dict):
            shell.user_ns.update(value)


shell_pool = ShellPool()
