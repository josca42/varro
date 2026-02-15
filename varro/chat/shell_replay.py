from __future__ import annotations

from pydantic_ai.messages import BaseToolCallPart, ModelMessage, ModelResponse

from varro.agent.env import Environment


async def restore_shell_namespace(env: Environment, msgs: list[ModelMessage]) -> None:
    for msg in msgs:
        if not isinstance(msg, ModelResponse):
            continue
        for part in msg.parts:
            if not isinstance(part, BaseToolCallPart):
                continue
            kwargs = part.args_as_dict()
            if part.tool_name == "Sql":
                if kwargs.get("df_name"):
                    try:
                        env.sql(**kwargs)
                    except Exception:
                        continue
                continue
            if part.tool_name != "Jupyter":
                continue
            try:
                await env.jupyter(**kwargs)
            except Exception:
                continue
