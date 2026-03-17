from __future__ import annotations

import asyncio
from types import SimpleNamespace

from fasthtml.common import to_xml

from app.routes import chat as chat_routes


def test_chat_run_start_blocks_when_balance_is_not_positive(monkeypatch) -> None:
    monkeypatch.setattr(chat_routes, "has_positive_balance", lambda _user_id: False)

    def should_not_create(_chat):
        raise AssertionError("chat should not be created when balance is insufficient")

    req = SimpleNamespace(
        state=SimpleNamespace(
            chats=SimpleNamespace(
                get=lambda _chat_id: None,
                create=should_not_create,
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

    assert isinstance(response, tuple)
    html = "".join(to_xml(part) for part in response)
    assert "Insufficient balance" in html
    assert 'value="gemini_pro" selected' in html
    assert "outerHTML:#chat-form" in html
