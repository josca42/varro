from __future__ import annotations

import asyncio
from decimal import Decimal
from types import SimpleNamespace

from app.routes import payments as payment_routes


class _FakeWebhookRequest:
    def __init__(self, payload: bytes = b"{}", signature: str = "sig"):
        self._payload = payload
        self.headers = {"stripe-signature": signature}

    async def body(self) -> bytes:
        return self._payload


def test_create_checkout_session_rejects_invalid_amount() -> None:
    req = SimpleNamespace(url=SimpleNamespace(scheme="https"), headers={"host": "varro.local"})
    sess = {"user_id": 7}

    response = payment_routes.create_checkout_session(req=req, sess=sess, amount_dkk="12.345")

    assert response.status_code == 400


def test_create_checkout_session_builds_dkk_checkout(monkeypatch) -> None:
    req = SimpleNamespace(url=SimpleNamespace(scheme="https"), headers={"host": "varro.local"})
    sess = {"user_id": 7}
    captured = {}

    monkeypatch.setattr(payment_routes, "stripe_secret_key", lambda: "sk_test_value")
    monkeypatch.setattr(payment_routes, "app_base_url", lambda _req: "https://varro.local")
    monkeypatch.setattr(
        payment_routes.crud.user,
        "get",
        lambda _user_id: SimpleNamespace(email="user@example.com"),
    )

    def fake_create(**kwargs):
        captured.update(kwargs)
        return SimpleNamespace(url="https://checkout.stripe.test/session")

    monkeypatch.setattr(payment_routes.stripe.checkout.Session, "create", fake_create)

    response = payment_routes.create_checkout_session(req=req, sess=sess, amount_dkk="100")

    assert response.status_code == 303
    assert response.headers["location"] == "https://checkout.stripe.test/session"
    assert captured["line_items"][0]["price_data"]["currency"] == "dkk"
    assert captured["line_items"][0]["price_data"]["unit_amount"] == 10000
    assert captured["metadata"]["user_id"] == "7"


def test_stripe_webhook_rejects_invalid_signature(monkeypatch) -> None:
    req = _FakeWebhookRequest()

    monkeypatch.setattr(payment_routes, "stripe_secret_key", lambda: "sk_test_value")
    monkeypatch.setattr(payment_routes, "webhook_secret", lambda: "whsec_test")
    monkeypatch.setattr(
        payment_routes.stripe.Webhook,
        "construct_event",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(ValueError("bad sig")),
    )

    response = asyncio.run(payment_routes.stripe_webhook(req))

    assert response.status_code == 400


def test_stripe_webhook_credits_paid_checkout(monkeypatch) -> None:
    req = _FakeWebhookRequest()
    captured = {}

    event = SimpleNamespace(
        id="evt_1",
        type="checkout.session.completed",
        data=SimpleNamespace(
            object=SimpleNamespace(
                id="cs_1",
                metadata={"user_id": "7"},
                amount_total=5000,
                currency="dkk",
                payment_status="paid",
                payment_intent="pi_1",
            )
        ),
    )

    monkeypatch.setattr(payment_routes, "stripe_secret_key", lambda: "sk_test_value")
    monkeypatch.setattr(payment_routes, "webhook_secret", lambda: "whsec_test")
    monkeypatch.setattr(
        payment_routes.stripe.Webhook,
        "construct_event",
        lambda *_args, **_kwargs: event,
    )

    def fake_credit(**kwargs):
        captured.update(kwargs)
        return True

    monkeypatch.setattr(payment_routes, "_credit_user_for_checkout", fake_credit)

    response = asyncio.run(payment_routes.stripe_webhook(req))

    assert response.status_code == 200
    assert captured["stripe_event_id"] == "evt_1"
    assert captured["checkout_session_id"] == "cs_1"
    assert captured["user_id"] == 7
    assert captured["amount_dkk"] == Decimal("50")
