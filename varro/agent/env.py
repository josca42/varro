from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pandas as pd
from sqlalchemy import text

from varro.agent.bash import run_bash_command
from varro.agent.ipython_shell import TerminalInteractiveShell
from varro.agent.utils import show_element
from varro.chat.runtime_state import load_bash_cwd, save_bash_cwd
from varro.data.utils import df_preview
from varro.db.db import engine


@dataclass(frozen=True)
class StepResult:
    """Immutable observation returned by an environment step."""

    text: str
    content: list[Any] | None = None
    has_ui_content: bool = False


class Environment:
    """Sandboxed execution environment for one chat session.

    Owns mutable state: IPython namespace, bash cwd.
    Methods are step functions: (action_args) -> StepResult.
    """

    def __init__(
        self, *, user_id: int, chat_id: int, shell: TerminalInteractiveShell
    ):
        self.user_id = user_id
        self.chat_id = chat_id
        self._shell = shell
        self._bash_cwd = load_bash_cwd(user_id, chat_id)

    @property
    def shell(self) -> TerminalInteractiveShell:
        return self._shell

    def sql(self, query: str, df_name: str | None = None) -> StepResult:
        with engine.connect() as conn:
            df = pd.read_sql(text(query), conn)
        if df_name:
            self._shell.user_ns[df_name] = df
            max_rows = 20 if len(df) < 21 else 5
            return StepResult(
                text=f"Stored as {df_name}\n{df_preview(df, max_rows=max_rows)}"
            )
        return StepResult(text=df_preview(df, max_rows=30))

    async def jupyter(
        self, code: str, show: list[str] | None = None
    ) -> StepResult:
        res = self._shell.run_cell(code)
        if res.error_before_exec:
            raise RuntimeError(repr(res.error_before_exec))
        if res.error_in_exec:
            raise RuntimeError(repr(res.error_in_exec))

        if not show:
            return StepResult(text=res.stdout)

        elements = []
        for name in show:
            element = self._shell.user_ns.get(name)
            rendered = await show_element(element)
            elements.append(rendered)

        return StepResult(
            text=res.stdout,
            content=elements if elements else None,
            has_ui_content=bool(elements),
        )

    def bash(self, command: str) -> StepResult:
        output, self._bash_cwd = run_bash_command(
            self.user_id, self._bash_cwd, command
        )
        save_bash_cwd(self.user_id, self.chat_id, self._bash_cwd)
        return StepResult(text=output)
