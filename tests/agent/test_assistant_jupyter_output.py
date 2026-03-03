from __future__ import annotations

import asyncio
import importlib
from types import SimpleNamespace

import pytest

from varro.agent.shell import JUPYTER_INITIAL_IMPORTS, get_shell


@pytest.fixture
def assistant_module(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")

    import logfire

    monkeypatch.setattr(logfire, "configure", lambda **kwargs: None)
    monkeypatch.setattr(logfire, "instrument_pydantic_ai", lambda: None)

    utils = importlib.import_module("varro.agent.utils")
    monkeypatch.setattr(utils, "get_dim_tables", lambda: ())

    assistant = importlib.import_module("varro.agent.assistant")
    return importlib.reload(assistant)


def _ctx_with_shell():
    shell = get_shell()
    shell.run_cell(JUPYTER_INITIAL_IMPORTS)
    return SimpleNamespace(deps=SimpleNamespace(shell=shell))


def test_jupyter_returns_only_printed_stdout_for_expression_result(assistant_module):
    ctx = _ctx_with_shell()

    result = asyncio.run(assistant_module.Jupyter(ctx, code='print("ok")\n1 + 1', show=[]))

    assert result.return_value == "ok\n"
    assert result.metadata == {"ui": {"has_tool_content": False}}


def test_jupyter_suppresses_figure_repr_when_showing_plotly(assistant_module, monkeypatch):
    seen = {}

    async def fake_show_element(element):
        seen["type"] = type(element).__name__
        return "rendered"

    monkeypatch.setattr(assistant_module, "show_element", fake_show_element)
    ctx = _ctx_with_shell()

    result = asyncio.run(
        assistant_module.Jupyter(
            ctx,
            code="\n".join(
                [
                    "df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 4]})",
                    "fig = px.line(df, x='x', y='y')",
                    "fig.add_hline(y=3)",
                ]
            ),
            show=["fig"],
        )
    )

    assert result.return_value == ""
    assert "Figure(" not in result.return_value
    assert result.content == ["rendered"]
    assert seen["type"] == "Figure"
    assert result.metadata == {"ui": {"has_tool_content": True}}


def test_jupyter_returns_empty_text_without_show_for_plotly_expression(assistant_module):
    ctx = _ctx_with_shell()

    result = asyncio.run(
        assistant_module.Jupyter(
            ctx,
            code="\n".join(
                [
                    "df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 4]})",
                    "fig = px.line(df, x='x', y='y')",
                    "fig.add_hline(y=3)",
                ]
            ),
            show=[],
        )
    )

    assert result.return_value == ""
    assert "Figure(" not in result.return_value
    assert result.metadata == {"ui": {"has_tool_content": False}}


def test_jupyter_uses_shell_render_show_when_available(assistant_module):
    class _ProxyShell:
        def __init__(self):
            self.user_ns = {}

        def run_cell(self, code: str):
            return SimpleNamespace(
                stdout="ok\n",
                error_before_exec=None,
                error_in_exec=None,
            )

        async def render_show(self, name: str):
            return f"rendered:{name}"

    ctx = SimpleNamespace(deps=SimpleNamespace(shell=_ProxyShell()))

    result = asyncio.run(
        assistant_module.Jupyter(ctx, code='print("ok")', show=["fig"])
    )

    assert result.return_value == "ok\n"
    assert result.content == ["rendered:fig"]
    assert result.metadata == {"ui": {"has_tool_content": True}}
