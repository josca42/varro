from __future__ import annotations

import asyncio
from types import SimpleNamespace

from fasthtml.common import Div, to_xml

import app.routes.chat as chat_routes
from ui.app.chat import ChatForm, ChatFormRunning
from varro.chat.session import ActiveRun


class _FakeChats:
    def __init__(self, chats: dict[int, object]):
        self._chats = dict(chats)
        self.deleted_ids: list[int] = []

    def get(self, chat_id: int | None, with_turns: bool = False):
        if chat_id is None:
            return None
        return self._chats.get(chat_id)

    def delete(self, chat):
        self.deleted_ids.append(chat.id)
        self._chats.pop(chat.id, None)


class _FakeUserSession:
    def __init__(self, user_id: int, chats: _FakeChats):
        self.user_id = user_id
        self.chats = chats
        self.sent: list[object] = []

    async def send(self, obj):
        self.sent.append(obj)


def test_stream_run_wraps_non_oob_blocks(monkeypatch):
    async def fake_run_agent(msg: str, session, chat_id: int, current_url: str | None):
        yield Div(f"plain:{msg}:{chat_id}:{current_url or ''}")
        yield Div("oob", id="x", hx_swap_oob="outerHTML:#x")

    monkeypatch.setattr(chat_routes, "run_agent", fake_run_agent)
    session = _FakeUserSession(user_id=1, chats=_FakeChats({}))

    asyncio.run(chat_routes._stream_run("Hej", session, chat_id=10, current_url="/dash"))

    assert len(session.sent) == 2
    wrapped = to_xml(session.sent[0])
    direct = to_xml(session.sent[1])
    assert 'hx-swap-oob="beforebegin:#chat-progress"' in wrapped
    assert "plain:Hej:10:/dash" in wrapped
    assert 'hx-swap-oob="outerHTML:#x"' in direct


def test_rollback_cancel_restores_existing_chat():
    existing_chat = SimpleNamespace(
        id=10,
        user_id=1,
        title="Existing chat",
        turns=[],
        created_at=None,
    )
    session = _FakeUserSession(user_id=1, chats=_FakeChats({10: existing_chat}))
    run = ActiveRun(
        run_id="run-1",
        chat_id=10,
        previous_chat_id=9,
        created_chat=False,
    )
    sess = {"user_id": 1, "chat_id": 10}

    asyncio.run(chat_routes._rollback_cancelled_run(session, sess, run))

    assert sess["chat_id"] == 10
    assert session.chats.deleted_ids == []
    rendered = to_xml(session.sent[-1])
    assert 'hx-swap-oob="outerHTML:#chat-panel"' in rendered
    assert 'name="chat_id" value="10"' in rendered


def test_rollback_cancel_deletes_new_chat_and_restores_previous_chat():
    previous_chat = SimpleNamespace(
        id=42,
        user_id=1,
        title="Previous chat",
        turns=[],
        created_at=None,
    )
    created_chat = SimpleNamespace(
        id=43,
        user_id=1,
        title=None,
        turns=[],
        created_at=None,
    )
    session = _FakeUserSession(
        user_id=1,
        chats=_FakeChats({42: previous_chat, 43: created_chat}),
    )
    run = ActiveRun(
        run_id="run-2",
        chat_id=43,
        previous_chat_id=42,
        created_chat=True,
    )
    sess = {"user_id": 1, "chat_id": 43}

    asyncio.run(chat_routes._rollback_cancelled_run(session, sess, run))

    assert sess["chat_id"] == 42
    assert session.chats.deleted_ids == [43]
    assert session.chats.get(43) is None
    rendered = to_xml(session.sent[-1])
    assert 'name="chat_id" value="42"' in rendered


def test_chat_cancel_route_is_idempotent(monkeypatch):
    class _CancelSpy:
        def __init__(self):
            self.calls: list[str | None] = []

        def cancel_active_run(self, run_id: str | None = None):
            self.calls.append(run_id)
            return True

    spy = _CancelSpy()

    class _RouteSessions:
        def get(self, user_id: int, sid: str):
            if user_id == 1 and sid == "sid-ok":
                return spy
            return None

        def touch(self, user_id: int | None, sid: str | None):
            return None

    monkeypatch.setattr(chat_routes, "sessions", _RouteSessions())

    first = chat_routes.chat_cancel("sid-ok", {"user_id": 1}, "run-1")
    second = chat_routes.chat_cancel("sid-missing", {"user_id": 1}, "run-2")

    assert first.status_code == 204
    assert second.status_code == 204
    assert spy.calls == ["run-1"]


def test_chat_form_running_renders_stop_button():
    html = to_xml(ChatFormRunning(chat_id=2, run_id="run-abc"))

    assert 'name="run_id" value="run-abc"' in html
    assert 'hx-post="/chat/cancel"' in html
    assert 'type="button"' in html
    assert "<rect " in html


def test_chat_form_idle_renders_submit_arrow():
    html = to_xml(ChatForm(chat_id=2))

    assert 'name="run_id" value=""' in html
    assert 'type="submit"' in html
    assert 'hx-post="/chat/cancel"' not in html
    assert '@keydown="' in html
    assert "$event.shiftKey" in html
    assert "requestSubmit()" in html
    assert '@submit="' in html
    assert "querySelector('#message-input')" in html
    assert "<polyline " in html
