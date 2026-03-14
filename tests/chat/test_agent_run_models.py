from __future__ import annotations

import asyncio
import importlib
from types import SimpleNamespace

import pytest
from pydantic_ai.usage import RunUsage


class _FakeRun:
    def __init__(self, *, result, usage: RunUsage, error: Exception | None = None):
        self.result = result
        self._usage = usage
        self._error = error

    def usage(self):
        return self._usage

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._error is not None:
            error = self._error
            self._error = None
            raise error
        raise StopAsyncIteration


class _IterContext:
    def __init__(self, run):
        self.run = run

    async def __aenter__(self):
        return self.run

    async def __aexit__(self, exc_type, exc, tb):
        return False


@pytest.fixture
def agent_run_module(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")

    import logfire

    monkeypatch.setattr(logfire, "configure", lambda **kwargs: None)
    monkeypatch.setattr(logfire, "instrument_pydantic_ai", lambda: None)

    utils = importlib.import_module("varro.agent.utils")
    monkeypatch.setattr(utils, "get_dim_tables", lambda: ())

    module = importlib.import_module("varro.chat.agent_run")
    return importlib.reload(module)


def test_run_agent_uses_selected_model(agent_run_module, monkeypatch) -> None:
    captured = {}
    charge_calls = []
    usage = RunUsage(requests=1, input_tokens=10, output_tokens=5)
    result = SimpleNamespace(
        response=SimpleNamespace(model_name=None),
        usage=lambda: usage,
        new_messages=lambda: [],
    )

    def fake_iter(*args, **kwargs):
        captured["args"] = args
        captured["kwargs"] = kwargs
        return _IterContext(_FakeRun(result=result, usage=usage))

    monkeypatch.setattr(agent_run_module, "load_messages_for_turns", lambda _turns: [])
    monkeypatch.setattr(agent_run_module.agent, "iter", fake_iter)
    monkeypatch.setattr(agent_run_module, "apply_model_charge", lambda **kw: charge_calls.append(kw))
    monkeypatch.setattr(
        agent_run_module,
        "turn_fp",
        lambda _user_id, _chat_id, _turn_idx: agent_run_module.DATA_DIR / "chat" / "1" / "2" / "1.mpk",
    )
    monkeypatch.setattr(agent_run_module, "save_turn_messages", lambda *_args: None)
    monkeypatch.setattr(agent_run_module, "save_turn_render_cache", lambda *_args: None)
    monkeypatch.setattr(agent_run_module.crud.turn, "create", lambda _turn: None)
    monkeypatch.setattr(agent_run_module.crud.chat, "update", lambda _chat: None)

    chats = SimpleNamespace(
        get=lambda _chat_id, with_turns=True: SimpleNamespace(
            id=2,
            turns=[SimpleNamespace(idx=0)],
            assistant_model="gemini_flash",
        )
    )

    async def collect():
        return [block async for block in agent_run_module.run_agent("Hello", user_id=1, chats=chats, shell=SimpleNamespace(), chat_id=2, run_id="run-1")]

    blocks = asyncio.run(collect())

    assert blocks == []
    assert captured["kwargs"]["model"] == "google-gla:gemini-3-flash-preview"
    assert captured["kwargs"]["model_settings"]["max_tokens"] == 16000
    assert charge_calls[0]["model_name"] == "gemini-3-flash-preview"


def test_run_agent_charges_selected_model_on_exception(agent_run_module, monkeypatch) -> None:
    charge_calls = []
    usage = RunUsage(requests=1, input_tokens=10, output_tokens=5)

    def fake_iter(*args, **kwargs):
        return _IterContext(
            _FakeRun(
                result=SimpleNamespace(),
                usage=usage,
                error=RuntimeError("boom"),
            )
        )

    monkeypatch.setattr(agent_run_module, "load_messages_for_turns", lambda _turns: [])
    monkeypatch.setattr(agent_run_module.agent, "iter", fake_iter)
    monkeypatch.setattr(agent_run_module, "apply_model_charge", lambda **kw: charge_calls.append(kw))

    chats = SimpleNamespace(
        get=lambda _chat_id, with_turns=True: SimpleNamespace(
            id=2,
            turns=[SimpleNamespace(idx=0)],
            assistant_model="gemini_pro",
        )
    )

    async def collect():
        async for _block in agent_run_module.run_agent("Hello", user_id=1, chats=chats, shell=SimpleNamespace(), chat_id=2, run_id="run-1"):
            pass

    with pytest.raises(RuntimeError, match="boom"):
        asyncio.run(collect())

    assert charge_calls[0]["model_name"] == "gemini-3.1-pro-preview"
