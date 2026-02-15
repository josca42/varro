from __future__ import annotations

import asyncio
from types import SimpleNamespace

from pydantic_ai.messages import ModelResponse, ToolCallPart

from varro.chat.shell_replay import restore_shell_namespace


def _make_env(sql_side_effect=None, jupyter_side_effect=None):
    env = SimpleNamespace()
    sql_calls = []
    jupyter_calls = []

    def fake_sql(**kwargs):
        if sql_side_effect:
            sql_side_effect(**kwargs)
        sql_calls.append(("Sql", kwargs))
        return SimpleNamespace(text="ok")

    async def fake_jupyter(**kwargs):
        if jupyter_side_effect:
            jupyter_side_effect(**kwargs)
        jupyter_calls.append(("Jupyter", kwargs))
        return SimpleNamespace(text="ok")

    env.sql = fake_sql
    env.jupyter = fake_jupyter
    env.sql_calls = sql_calls
    env.jupyter_calls = jupyter_calls
    return env


def test_restore_shell_namespace_replays_sql_and_jupyter():
    env = _make_env()

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

    asyncio.run(restore_shell_namespace(env=env, msgs=msgs))

    assert env.sql_calls == [
        ("Sql", {"query": "select 1", "df_name": "df_a"}),
    ]
    assert env.jupyter_calls == [
        ("Jupyter", {"code": "x = 1", "show": []}),
    ]


def test_restore_shell_namespace_ignores_jupyter_errors():
    def raise_error(**kwargs):
        raise RuntimeError("execution failed")

    env = _make_env(jupyter_side_effect=raise_error)

    msgs = [
        ModelResponse(
            parts=[ToolCallPart("Jupyter", {"code": "broken()", "show": []})],
            finish_reason="stop",
        )
    ]

    asyncio.run(restore_shell_namespace(env=env, msgs=msgs))
