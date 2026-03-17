from __future__ import annotations

import asyncio
from types import SimpleNamespace

from fasthtml.common import to_xml

from app.routes import chat as chat_routes


class _RunManagerStub:
    async def create_run(self, *, run_id: str, user_id: int, chat_id: int):
        return SimpleNamespace(run_id=run_id, user_id=user_id, chat_id=chat_id)

    async def attach_task(self, run_id: str, task) -> None:
        return None


def _close_task(coro):
    coro.close()
    return SimpleNamespace()


def test_chat_run_start_creates_chat_with_selected_model(monkeypatch) -> None:
    created = {}

    def fake_create(chat):
        created["chat"] = chat
        return SimpleNamespace(id=41, assistant_model=chat.assistant_model)

    monkeypatch.setattr(chat_routes, "has_positive_balance", lambda _user_id: True)
    monkeypatch.setattr(chat_routes, "run_manager", _RunManagerStub())
    monkeypatch.setattr(chat_routes.asyncio, "create_task", _close_task)

    req = SimpleNamespace(
        state=SimpleNamespace(
            chats=SimpleNamespace(
                get=lambda _chat_id: None,
                create=fake_create,
                update=lambda _chat: None,
            )
        )
    )
    sess = {"user_id": 7}

    response = asyncio.run(
        chat_routes.chat_run_start(
            msg="Hello",
            sess=sess,
            req=req,
            chat_id=None,
            current_url="/app",
            model_key="gemini_pro",
        )
    )

    html = "".join(to_xml(part) for part in response)

    assert created["chat"].assistant_model == "gemini_pro"
    assert sess["chat_id"] == 41
    assert 'value="gemini_pro" selected' in html


def test_chat_run_start_updates_existing_chat_model(monkeypatch) -> None:
    updates = []
    existing_chat = SimpleNamespace(id=11, assistant_model="anthropic_opus")

    monkeypatch.setattr(chat_routes, "has_positive_balance", lambda _user_id: True)
    monkeypatch.setattr(chat_routes, "run_manager", _RunManagerStub())
    monkeypatch.setattr(chat_routes.asyncio, "create_task", _close_task)

    req = SimpleNamespace(
        state=SimpleNamespace(
            chats=SimpleNamespace(
                get=lambda _chat_id: existing_chat,
                create=lambda _chat: None,
                update=lambda chat: updates.append(chat),
            )
        )
    )
    sess = {"user_id": 7}

    response = asyncio.run(
        chat_routes.chat_run_start(
            msg="Hello",
            sess=sess,
            req=req,
            chat_id=11,
            current_url="/app",
            model_key="gemini_flash",
        )
    )

    html = "".join(to_xml(part) for part in response)

    assert len(updates) == 1
    assert updates[0].id == 11
    assert updates[0].assistant_model == "gemini_flash"
    assert 'value="gemini_flash" selected' in html
