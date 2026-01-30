from __future__ import annotations

import json
import asyncio
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field
from pathlib import Path
from typing import Awaitable, Callable
from types import SimpleNamespace

import msgpack
import zstandard as zstd
from pydantic_ai.messages import ModelMessage, ModelResponse, BaseToolCallPart
from pydantic_ai import ModelMessagesTypeAdapter, ModelRetry
from pydantic_core import to_jsonable_python
from starlette.websockets import WebSocketState

from varro.agent.ipython_shell import (
    get_shell,
    TerminalInteractiveShell,
    JUPYTER_INITIAL_IMPORTS,
)
from varro.db.crud.chat import CrudChat
from varro.db.models.chat import Chat, Turn
from varro.db import crud

zstd_compressor = zstd.ZstdCompressor(level=3)
zstd_decompressor = zstd.ZstdDecompressor()


@dataclass
class UserSession:
    """In-memory session for a single user's chat interaction."""

    user_id: int
    sid: str
    chats: CrudChat
    send: Callable[[object], Awaitable[None]]
    ws: object

    shell: TerminalInteractiveShell = field(init=False)
    last_seen: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc), init=False
    )
    chat_id: int | None = field(default=None, init=False)
    msgs: list[ModelMessage] = field(default_factory=list, init=False)
    turn_idx: int = field(default=0, init=False)
    cached_prompts: dict[str, str] = field(default_factory=dict, init=False)

    def __post_init__(self):
        self.shell = get_shell()
        self.shell.run_cell(JUPYTER_INITIAL_IMPORTS)
        self.touch()

    def touch(self) -> None:
        self.last_seen = datetime.now(timezone.utc)

    async def start_chat(self, chat_id: int | None) -> None:
        """Initialize or restore a chat session."""
        self._reset_chat_state()

        if chat_id is None:
            return

        self.chat_id = chat_id
        chat = self.chats.get(chat_id, with_turns=True)
        if not chat:
            return

        for turn in chat.turns:
            loaded = self._load_turn(Path(turn.obj_fp))
            self.msgs.extend(loaded)

        self.turn_idx = len(chat.turns)

        if self.msgs:
            await self._restore_shell_namespace()

    def save_turn(self, new_msgs: list[ModelMessage], user_text: str) -> None:
        """Save a completed turn to disk and database."""
        fp = self._turn_filepath()
        self._save_turn(new_msgs, fp)

        crud.turn.create(
            Turn(
                chat_id=self.chat_id,
                user_text=user_text,
                obj_fp=str(fp),
                idx=self.turn_idx,
            )
        )
        crud.chat.update(Chat(id=self.chat_id, updated_at=datetime.now(timezone.utc)))
        self.msgs.extend(new_msgs)
        self.turn_idx += 1

    def delete_from_idx(self, idx: int) -> None:
        """Delete turns from idx onwards (for edit functionality)."""
        deleted_paths = crud.turn.delete_from_idx(self.chat_id, idx)

        for fp in deleted_paths:
            path = Path(fp)
            if path.exists():
                path.unlink()

        chat = self.chats.get(self.chat_id, with_turns=True)
        self.msgs = []
        for turn in chat.turns:
            loaded = self._load_turn(Path(turn.obj_fp))
            self.msgs.extend(loaded)

        self.turn_idx = idx

    def cleanup(self) -> None:
        """Cleanup session resources on disconnect."""
        if self.shell:
            self.shell.reset(new_session=False)
            if self.shell.history_manager:
                self.shell.history_manager.end_session()

    async def close_ws(self) -> None:
        if self.ws is None:
            return
        try:
            if (
                getattr(self.ws, "application_state", None)
                is WebSocketState.DISCONNECTED
                or getattr(self.ws, "client_state", None) is WebSocketState.DISCONNECTED
            ):
                return
            await self.ws.close()
        except RuntimeError:
            return
        finally:
            self.ws = None

    def _reset_chat_state(self) -> None:
        """Reset state for a new/different chat."""
        self.chat_id = None
        self.msgs = []
        self.turn_idx = 0
        if self.shell:
            self.shell.reset(new_session=True)
            self.shell.run_cell(JUPYTER_INITIAL_IMPORTS)

    def _turn_filepath(self) -> Path:
        """Generate filepath for current turn."""
        base = Path(f"data/chats/{self.user_id}/{self.chat_id}")
        base.mkdir(parents=True, exist_ok=True)
        return base / f"{self.turn_idx}.mpk"

    async def _restore_shell_namespace(self) -> None:
        """Re-run tool calls to restore shell state."""
        from varro.agent.assistant import sql_query, jupyter_notebook

        ctx = SimpleNamespace(deps=self)
        for msg in self.msgs:
            if not isinstance(msg, ModelResponse):
                continue

            for part in msg.parts:
                if not isinstance(part, BaseToolCallPart):
                    continue

                args = part.args or {}
                if isinstance(args, str):
                    args = json.loads(args)

                if part.tool_name == "sql_query":
                    df_name = args.get("df_name")
                    if df_name:
                        sql_query(ctx, args.get("query", ""), df_name)

                elif part.tool_name == "jupyter_notebook":
                    try:
                        await jupyter_notebook(ctx, args.get("code", ""), show=[])
                    except ModelRetry as e:
                        continue

    @staticmethod
    def _save_turn(msgs: list[ModelMessage], fp: Path) -> None:
        """Save messages to disk as msgpack+zstd."""
        msg_objs = to_jsonable_python(msgs, bytes_mode="base64")
        packed = msgpack.packb(msg_objs, use_bin_type=True, strict_types=True)
        compressed = zstd_compressor.compress(packed)
        fp.write_bytes(compressed)

    @staticmethod
    def _load_turn(fp: Path) -> list[ModelMessage]:
        """Load messages from disk."""
        compressed = fp.read_bytes()
        packed = zstd_decompressor.decompress(compressed)
        obj = msgpack.unpackb(packed, raw=False)
        return ModelMessagesTypeAdapter.validate_python(obj)


class SessionManager:
    """Manages all active user sessions."""

    def __init__(self):
        self._sessions: dict[int, dict[str, UserSession]] = {}
        self._cleanup_task: asyncio.Task | None = None

    def get(self, user_id: int, sid: str) -> UserSession | None:
        return self._sessions.get(user_id, {}).get(sid)

    def find_by_ws(self, user_id: int, ws: object) -> UserSession | None:
        sessions = self._sessions.get(user_id, {})
        for session in sessions.values():
            if session.ws is ws:
                return session
        return None

    async def create(
        self,
        user_id: int,
        sid: str,
        chats: CrudChat,
        send: Callable[[object], Awaitable[None]],
        ws: object,
    ) -> UserSession:
        """Create session, replacing any existing one for this sid."""
        sessions = self._sessions.setdefault(user_id, {})
        if sid in sessions:
            old_session = sessions[sid]
            await old_session.close_ws()
            old_session.cleanup()

        session = UserSession(user_id=user_id, sid=sid, chats=chats, send=send, ws=ws)
        sessions[sid] = session
        return session

    def remove(self, user_id: int, sid: str) -> None:
        """Remove and cleanup a session."""
        sessions = self._sessions.get(user_id)
        if not sessions:
            return
        if session := sessions.pop(sid, None):
            session.cleanup()
        if not sessions:
            self._sessions.pop(user_id, None)

    async def close_and_remove(self, user_id: int, sid: str) -> None:
        session = self.get(user_id, sid)
        if not session:
            return
        await session.close_ws()
        self.remove(user_id, sid)

    def touch(self, user_id: int, sid: str) -> None:
        session = self.get(user_id, sid)
        if session:
            session.touch()

    async def evict_idle(self, ttl: timedelta) -> None:
        now = datetime.now(timezone.utc)
        to_evict: list[tuple[int, str]] = []
        for user_id, sessions in self._sessions.items():
            for sid, session in sessions.items():
                if now - session.last_seen > ttl:
                    to_evict.append((user_id, sid))
        for user_id, sid in to_evict:
            await self.close_and_remove(user_id, sid)

    def start_cleanup_task(
        self, ttl: timedelta = timedelta(minutes=20), interval: int = 60
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
