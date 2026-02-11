from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Awaitable, Callable

from varro.agent.ipython_shell import (
    JUPYTER_INITIAL_IMPORTS,
    TerminalInteractiveShell,
    get_shell,
)
from varro.chat.shell_replay import restore_shell_namespace
from varro.db.crud.chat import CrudChat


@dataclass
class _ShellReplayDeps:
    user_id: int
    chat_id: int
    shell: TerminalInteractiveShell

    def request_current_url(self) -> str:
        return "/"


@dataclass
class ActiveRun:
    run_id: str
    chat_id: int
    previous_chat_id: int | None
    created_chat: bool
    task: asyncio.Task | None = None


@dataclass
class UserSession:
    """In-memory session for one websocket tab."""

    user_id: int
    sid: str
    chats: CrudChat
    send: Callable[[object], Awaitable[None]]
    ws: object

    shell: TerminalInteractiveShell = field(init=False)
    shell_chat_id: int | None = field(default=None, init=False)
    active_run: ActiveRun | None = field(default=None, init=False)

    def __post_init__(self):
        self.shell = get_shell()
        self.shell.run_cell(JUPYTER_INITIAL_IMPORTS)

    async def ensure_shell_for_chat(self, chat_id: int, msgs: list) -> None:
        if self.shell_chat_id == chat_id:
            return

        self.shell.reset(new_session=True)
        self.shell.run_cell(JUPYTER_INITIAL_IMPORTS)
        deps = _ShellReplayDeps(
            user_id=self.user_id,
            chat_id=chat_id,
            shell=self.shell,
        )
        if msgs:
            await restore_shell_namespace(self.shell, deps, msgs)
        self.shell_chat_id = chat_id

    def start_run(
        self,
        *,
        run_id: str,
        chat_id: int,
        previous_chat_id: int | None,
        created_chat: bool,
    ) -> bool:
        active = self.active_run
        if active:
            if active.task is None or not active.task.done():
                return False
        self.active_run = ActiveRun(
            run_id=run_id,
            chat_id=chat_id,
            previous_chat_id=previous_chat_id,
            created_chat=created_chat,
        )
        return True

    def attach_run_task(self, run_id: str, task: asyncio.Task) -> None:
        active = self.active_run
        if not active or active.run_id != run_id:
            task.cancel()
            return
        active.task = task

    def cancel_active_run(self, run_id: str | None = None) -> bool:
        active = self.active_run
        if not active:
            return False
        if run_id is not None and active.run_id != run_id:
            return False
        if active.task and not active.task.done():
            active.task.cancel()
            return True
        return False

    def clear_run(self, run_id: str | None = None) -> None:
        if self.active_run is None:
            return
        if run_id is not None and self.active_run.run_id != run_id:
            return
        self.active_run = None

    def cleanup(self) -> None:
        self.cancel_active_run()
        self.clear_run()
        if self.shell:
            self.shell.reset(new_session=False)
            if self.shell.history_manager:
                self.shell.history_manager.end_session()
            self.shell_chat_id = None

    async def close_ws(self) -> None:
        if self.ws is None:
            return
        try:
            await self.ws.close()
        except Exception:
            pass
        finally:
            self.ws = None


@dataclass
class SessionEntry:
    session: UserSession
    last_seen: datetime


class SessionManager:
    """Manages active websocket sessions."""

    def __init__(self):
        self._sessions: dict[int, dict[str, SessionEntry]] = {}
        self._cleanup_task: asyncio.Task | None = None

    def get(self, user_id: int, sid: str) -> UserSession | None:
        entry = self._sessions.get(user_id, {}).get(sid)
        return entry.session if entry else None

    def find_by_ws(self, user_id: int, ws: object) -> UserSession | None:
        entries = self._sessions.get(user_id, {})
        for entry in entries.values():
            if entry.session.ws is ws:
                return entry.session
        return None

    async def create(
        self,
        user_id: int,
        sid: str,
        chats: CrudChat,
        send: Callable[[object], Awaitable[None]],
        ws: object,
    ) -> UserSession:
        entries = self._sessions.setdefault(user_id, {})
        if sid in entries:
            old = entries[sid].session
            await old.close_ws()
            old.cleanup()

        session = UserSession(user_id=user_id, sid=sid, chats=chats, send=send, ws=ws)
        entries[sid] = SessionEntry(
            session=session,
            last_seen=datetime.now(timezone.utc),
        )
        return session

    def remove(self, user_id: int, sid: str) -> None:
        entries = self._sessions.get(user_id)
        if not entries:
            return
        entry = entries.pop(sid, None)
        if entry:
            entry.session.cleanup()
        if not entries:
            self._sessions.pop(user_id, None)

    async def close_and_remove(self, user_id: int, sid: str) -> None:
        session = self.get(user_id, sid)
        if not session:
            return
        await session.close_ws()
        self.remove(user_id, sid)

    def touch(self, user_id: int, sid: str) -> None:
        entry = self._sessions.get(user_id, {}).get(sid)
        if entry:
            entry.last_seen = datetime.now(timezone.utc)

    async def evict_idle(self, ttl: timedelta) -> None:
        now = datetime.now(timezone.utc)
        to_evict: list[tuple[int, str]] = []
        for user_id, entries in self._sessions.items():
            for sid, entry in entries.items():
                if now - entry.last_seen > ttl:
                    to_evict.append((user_id, sid))
        for user_id, sid in to_evict:
            await self.close_and_remove(user_id, sid)

    def start_cleanup_task(
        self,
        ttl: timedelta = timedelta(minutes=20),
        interval: int = 60,
    ) -> None:
        if self._cleanup_task and not self._cleanup_task.done():
            return

        async def _loop() -> None:
            while True:
                await asyncio.sleep(interval)
                await self.evict_idle(ttl)

        self._cleanup_task = asyncio.create_task(_loop())

    def stop_cleanup_task(self) -> None:
        if self._cleanup_task and not self._cleanup_task.done():
            self._cleanup_task.cancel()


sessions = SessionManager()
