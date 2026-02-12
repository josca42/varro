from __future__ import annotations

import asyncio
from types import SimpleNamespace

from fasthtml.common import Div, to_xml

import app.routes.chat as chat_routes
from ui.app.chat import ChatForm, ChatFormRunning


def test_stream_block_wraps_non_oob_blocks():
    plain_html = to_xml(chat_routes._stream_block(Div("plain")))
    oob_html = to_xml(chat_routes._stream_block(Div("oob", id="x", hx_swap_oob="outerHTML:#x")))

    assert 'hx-swap-oob="beforebegin:#chat-progress"' in plain_html
    assert "plain" in plain_html
    assert 'hx-swap-oob="outerHTML:#x"' in oob_html
    assert ">oob<" in oob_html


def test_chat_form_running_renders_run_specific_cancel_button():
    html = to_xml(ChatFormRunning(chat_id=2, run_id="run-abc"))

    assert 'name="run_id" value="run-abc"' in html
    assert 'hx-post="/chat/runs/run-abc/cancel"' in html
    assert 'type="button"' in html
    assert "<rect " in html


def test_chat_form_idle_posts_to_run_start_endpoint():
    html = to_xml(ChatForm(chat_id=2))

    assert 'hx-post="/chat/runs"' in html
    assert 'hx-swap="none"' in html
    assert 'hx-post="/chat/runs/' not in html
    assert 'name="run_id" value=""' in html
    assert 'type="submit"' in html
    assert "<polyline " in html


def test_chat_run_cancel_sets_session_chat_and_calls_cancel(monkeypatch):
    class _RunManagerStub:
        def __init__(self):
            self.cancel_calls: list[str] = []
            self.run = SimpleNamespace(
                run_id="run-1",
                user_id=1,
                chat_id=50,
            )

        async def get_for_user(self, run_id: str, user_id: int):
            if run_id == "run-1" and user_id == 1:
                return self.run
            return None

        async def cancel(self, run_id: str):
            self.cancel_calls.append(run_id)
            return True

    stub = _RunManagerStub()
    monkeypatch.setattr(chat_routes, "run_manager", stub)

    sess = {"user_id": 1, "chat_id": 1}
    response = asyncio.run(chat_routes.chat_run_cancel("run-1", sess))

    assert response.status_code == 204
    assert sess["chat_id"] == 50
    assert stub.cancel_calls == ["run-1"]


def test_chat_run_cancel_returns_404_for_missing_run(monkeypatch):
    class _RunManagerStub:
        async def get_for_user(self, run_id: str, user_id: int):
            return None

    monkeypatch.setattr(chat_routes, "run_manager", _RunManagerStub())

    sess = {"user_id": 1}
    response = asyncio.run(chat_routes.chat_run_cancel("missing", sess))

    assert response.status_code == 404
