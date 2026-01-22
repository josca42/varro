from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime
from types import SimpleNamespace
from typing import Any
from typing_extensions import Dict

from pydantic_ai import ModelMessagesTypeAdapter
from pydantic_ai.messages import ModelMessage, ModelResponse, BaseToolCallPart
from pydantic_core import to_jsonable_python

from varro.agent.assistant import SessionStore, sql_query, jupyter_notebook
from varro.db import crud
from varro.db.crud.chat import CrudChat
from varro.db.models.chat import Chat, Message
from varro.db.models.user import User
from varro.agent.ipython_shell import get_shell, TerminalInteractiveShell
from pydantic_ai.run import RunResult


@dataclass
class ChatSession:
    user: User
    chat_id: int
    chats: CrudChat
    shell: TerminalInteractiveShell | None = None
    cached_prompts: Dict[str, str] = field(default_factory=dict)
    shell_imports: bool = False
    msgs = []

    def __init__(self, user: User, chats: CrudChat, chat_id: int):
        self.user = user
        self.cached_prompts = {}
        self.shell = get_shell()
        self.shell_imports = False
        self.chats = chats
        self.chat_id = chat_id

    async def start(self):
        self.msgs = self.chats.get(self.chat_id, with_msgs=True).messages
        if len(self.msgs) > 1:
            await self._restore_shell_namespace()

    def save_run_msgs(self, run: RunResult):
        new_msgs = run.result.new_messages_json().decode("utf-8")
        crud.message.create(Message(chat_id=self.chat_id, content=new_msgs))

    def end(self) -> None:
        self.shell.reset(new_session=False)
        self.shell.history_manager.end_session()

    async def _restore_shell_namespace(self) -> None:
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
