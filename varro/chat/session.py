from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Awaitable, Callable

import msgpack
import zstandard as zstd
from pydantic_ai.messages import ModelMessage, ModelResponse, BaseToolCallPart
from pydantic_ai import ModelMessagesTypeAdapter
from pydantic_core import to_jsonable_python

from varro.agent.ipython_shell import get_shell, TerminalInteractiveShell
from varro.db.crud.chat import CrudChat
from varro.db.models.chat import Turn
from varro.db.models.user import User
from varro.db import crud

zstd_compressor = zstd.ZstdCompressor(level=3)
zstd_decompressor = zstd.ZstdDecompressor()


@dataclass
class UserSession:
    """In-memory session for a single user's chat interaction."""

    user: User
    chats: CrudChat
    send: Callable[[object], Awaitable[None]]

    shell: TerminalInteractiveShell = field(init=False)
    chat_id: int | None = field(default=None, init=False)
    msgs: list[ModelMessage] = field(default_factory=list, init=False)
    turn_idx: int = field(default=0, init=False)
    cached_prompts: dict[str, str] = field(default_factory=dict, init=False)
    shell_imports: bool = field(default=False, init=False)

    def __post_init__(self):
        self.shell = get_shell()

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

    def _reset_chat_state(self) -> None:
        """Reset state for a new/different chat."""
        self.chat_id = None
        self.msgs = []
        self.turn_idx = 0
        self.shell_imports = False
        if self.shell:
            self.shell.reset(new_session=True)

    def _turn_filepath(self) -> Path:
        """Generate filepath for current turn."""
        base = Path(f"data/chats/{self.user.id}/{self.chat_id}")
        base.mkdir(parents=True, exist_ok=True)
        return base / f"{self.turn_idx}.mpk"

    async def _restore_shell_namespace(self) -> None:
        """Re-run tool calls to restore shell state."""
        from varro.agent.assistant import sql_query, jupyter_notebook

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
                        sql_query(self, args.get("query", ""), df_name)

                elif part.tool_name == "jupyter_notebook":
                    await jupyter_notebook(self, args.get("code", ""), show=[])

    @staticmethod
    def _save_turn(msgs: list[ModelMessage], fp: Path) -> None:
        """Save messages to disk as msgpack+zstd."""
        msg_objs = to_jsonable_python(msgs)
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
        self._sessions: dict[int, UserSession] = {}

    def get(self, user_id: int) -> UserSession | None:
        return self._sessions.get(user_id)

    def create(
        self, user: User, chats: CrudChat, send: Callable[[object], Awaitable[None]]
    ) -> UserSession:
        """Create session, replacing any existing one for this user."""
        if user.id in self._sessions:
            self._sessions[user.id].cleanup()

        session = UserSession(user=user, chats=chats, send=send)
        self._sessions[user.id] = session
        return session

    def remove(self, user_id: int) -> None:
        """Remove and cleanup a session."""
        if session := self._sessions.pop(user_id, None):
            session.cleanup()


sessions = SessionManager()
