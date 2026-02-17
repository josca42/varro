from __future__ import annotations

import asyncio
import sys
from types import ModuleType, SimpleNamespace

from pydantic_ai import ModelRetry
from pydantic_ai.messages import ModelResponse, ToolCallPart

from varro.chat.shell_replay import restore_shell_namespace


def test_restore_shell_namespace_replays_sql_and_jupyter(monkeypatch):
    calls = []

    fake_assistant = ModuleType("varro.agent.assistant")

    def fake_sql(ctx, **kwargs):
        calls.append(("Sql", kwargs, ctx.deps.chat_id))

    async def fake_jupyter(ctx, **kwargs):
        calls.append(("Jupyter", kwargs, ctx.deps.chat_id))

    fake_assistant.Sql = fake_sql
    fake_assistant.Jupyter = fake_jupyter
    monkeypatch.setitem(sys.modules, "varro.agent.assistant", fake_assistant)

    msgs = [
        ModelResponse(
            parts=[
                ToolCallPart("Sql", {"query": "select 1", "df_name": "df_a"}),
                ToolCallPart("Sql", {"query": "select 2"}),
                ToolCallPart("Jupyter", {"code": "x = 1", "show": []}),
                ToolCallPart("Bash", {"command": "pwd"}),
            ],
            finish_reason="stop",
        )
    ]
    deps = SimpleNamespace(chat_id=13)

    asyncio.run(restore_shell_namespace(shell=SimpleNamespace(), deps=deps, msgs=msgs))

    assert calls == [
        ("Sql", {"query": "select 1", "df_name": "df_a"}, 13),
        ("Jupyter", {"code": "x = 1", "show": []}, 13),
    ]


def test_restore_shell_namespace_ignores_jupyter_model_retry(monkeypatch):
    fake_assistant = ModuleType("varro.agent.assistant")

    def fake_sql(ctx, **kwargs):
        return None

    async def fake_jupyter(ctx, **kwargs):
        raise ModelRetry("execution failed")

    fake_assistant.Sql = fake_sql
    fake_assistant.Jupyter = fake_jupyter
    monkeypatch.setitem(sys.modules, "varro.agent.assistant", fake_assistant)

    msgs = [
        ModelResponse(
            parts=[ToolCallPart("Jupyter", {"code": "broken()", "show": []})],
            finish_reason="stop",
        )
    ]

    asyncio.run(
        restore_shell_namespace(shell=SimpleNamespace(), deps=SimpleNamespace(), msgs=msgs)
    )
