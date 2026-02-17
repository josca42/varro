from __future__ import annotations

from types import SimpleNamespace

from pydantic_ai import ModelRetry
from pydantic_ai.messages import BaseToolCallPart, ModelMessage, ModelResponse


async def restore_shell_namespace(shell, deps, msgs: list[ModelMessage]) -> None:
    from varro.agent.assistant import Jupyter, Sql

    ctx = SimpleNamespace(deps=deps)
    for msg in msgs:
        if not isinstance(msg, ModelResponse):
            continue
        for part in msg.parts:
            if not isinstance(part, BaseToolCallPart):
                continue
            kwargs = part.args_as_dict()
            if part.tool_name == "Sql":
                if kwargs.get("df_name"):
                    Sql(ctx, **kwargs)
                continue
            if part.tool_name != "Jupyter":
                continue
            try:
                await Jupyter(ctx, **kwargs)
            except ModelRetry:
                continue
