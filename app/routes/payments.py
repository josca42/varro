from __future__ import annotations

import os
from decimal import Decimal, InvalidOperation

import stripe
from fasthtml.common import A, APIRouter, Div, H2, P, RedirectResponse, Response
from sqlalchemy import or_, update
from sqlmodel import Session, select

from varro.config import settings
from varro.db import crud
from varro.db.db import user_engine
from varro.db.models.payment import StripePayment
from varro.db.models.user import User

ar = APIRouter()

CURRENCY = "dkk"
TOPUP_PRODUCT_NAME = "Varro account balance top-up"


def config_value(key: str) -> str | None:
    return settings.get(key) or os.environ.get(key)


def stripe_secret_key() -> str:
    key = config_value("STRIPE_SECRET_KEY")
    if not key:
        raise RuntimeError("STRIPE_SECRET_KEY is required.")
    return key


def webhook_secret() -> str:
    key = config_value("STRIPE_WEBHOOK_SECRET")
    if not key:
        raise RuntimeError("STRIPE_WEBHOOK_SECRET is required.")
    return key


def app_base_url(req) -> str:
    configured = config_value("APP_BASE_URL")
    if configured:
        return configured.rstrip("/")
    return f"{req.url.scheme}://{req.headers['host']}"


def parse_amount_dkk(raw_amount: str | None) -> Decimal:
    if raw_amount is None:
        raise ValueError("amount_dkk is required")
    value = raw_amount.strip()
    if not value:
        raise ValueError("amount_dkk is required")
    try:
        amount = Decimal(value)
    except InvalidOperation as exc:
        raise ValueError("Invalid amount") from exc
    rounded = amount.quantize(Decimal("0.01"))
    if rounded != amount:
        raise ValueError("Amount must use at most two decimals")
    if rounded <= 0:
        raise ValueError("Amount must be positive")
    return rounded


def to_minor_units(amount_dkk: Decimal) -> int:
    return int(amount_dkk * 100)


def _credit_user_for_checkout(
    *,
    stripe_event_id: str,
    checkout_session_id: str,
    payment_intent_id: str | None,
    user_id: int,
    amount_dkk: Decimal,
    currency: str,
    payment_status: str,
) -> bool:
    with Session(user_engine) as session, session.begin():
        duplicate_stmt = select(StripePayment.id).where(
            or_(
                StripePayment.checkout_session_id == checkout_session_id,
                StripePayment.stripe_event_id == stripe_event_id,
            )
        )
        if session.exec(duplicate_stmt).one_or_none() is not None:
            return False

        payment = StripePayment(
            user_id=user_id,
            checkout_session_id=checkout_session_id,
            stripe_event_id=stripe_event_id,
            payment_intent_id=payment_intent_id,
            amount_dkk=amount_dkk,
            currency=currency,
            payment_status=payment_status,
        )
        session.add(payment)

        increment_stmt = (
            update(User)
            .where(User.id == user_id)
            .values(balance=User.balance + amount_dkk)
            .execution_options(synchronize_session=False)
        )
        result = session.exec(increment_stmt)
        if result.rowcount != 1:
            raise RuntimeError(f"User not found for Stripe credit: {user_id}")

    return True


@ar("/payments/checkout", methods=["POST"])
def create_checkout_session(req, sess, amount_dkk: str | None = None):
    user_id = sess.get("user_id")
    if user_id is None:
        return Response(status_code=403)

    try:
        parsed_amount = parse_amount_dkk(amount_dkk)
    except ValueError as exc:
        return Response(str(exc), status_code=400)

    stripe.api_key = stripe_secret_key()
    db_user = crud.user.get(user_id)
    if not db_user:
        raise RuntimeError(f"User not found for Stripe checkout: {user_id}")
    checkout_session = stripe.checkout.Session.create(
        mode="payment",
        payment_method_types=["card"],
        customer_email=db_user.email,
        metadata={
            "user_id": str(user_id),
            "amount_dkk": f"{parsed_amount:.2f}",
        },
        line_items=[
            {
                "price_data": {
                    "currency": CURRENCY,
                    "product_data": {"name": TOPUP_PRODUCT_NAME},
                    "unit_amount": to_minor_units(parsed_amount),
                },
                "quantity": 1,
            }
        ],
        success_url=(
            f"{app_base_url(req)}/payments/success?checkout_sid={{CHECKOUT_SESSION_ID}}"
        ),
        cancel_url=f"{app_base_url(req)}/payments/cancel",
    )
    return RedirectResponse(checkout_session.url, status_code=303)


@ar("/payments/webhook", methods=["POST"])
async def stripe_webhook(req):
    stripe.api_key = stripe_secret_key()
    payload = await req.body()
    signature = req.headers.get("stripe-signature")
    try:
        event = stripe.Webhook.construct_event(payload, signature, webhook_secret())
    except Exception:
        return Response(status_code=400)

    if event.type != "checkout.session.completed":
        return Response(status_code=200)

    event_data = event.data.object
    if event_data.payment_status != "paid":
        return Response(status_code=200)

    currency = (event_data.currency or "").lower()
    if currency != CURRENCY:
        raise RuntimeError(f"Unsupported currency in Stripe webhook: {currency}")

    user_id = int(event_data.metadata["user_id"])
    amount_dkk = Decimal(event_data.amount_total) / 100
    _credit_user_for_checkout(
        stripe_event_id=event.id,
        checkout_session_id=event_data.id,
        payment_intent_id=event_data.payment_intent,
        user_id=user_id,
        amount_dkk=amount_dkk,
        currency=currency,
        payment_status=event_data.payment_status,
    )
    return Response(status_code=200)


@ar("/payments/success", methods=["GET"])
def payment_success(sess, checkout_sid: str | None = None):
    if not checkout_sid:
        return RedirectResponse("/settings", status_code=303)

    user_id = sess.get("user_id")
    if user_id is None:
        return RedirectResponse("/login", status_code=303)

    payment = crud.stripe_payment.get_paid_for_user_checkout(user_id, checkout_sid)
    if not payment:
        return Div(
            H2("Payment processing"),
            P("Your payment is being confirmed. Refresh in a moment."),
            A("Back to settings", href="/settings", cls="btn btn-outline btn-sm mt-4"),
            cls="p-6 space-y-2",
        )

    db_user = crud.user.get(user_id)
    balance_text = f"{db_user.balance:.2f}" if db_user else "0.00"
    return Div(
        H2("Balance updated"),
        P(f"Added {payment.amount_dkk:.2f} DKK to your account."),
        P(f"Current balance: {balance_text} DKK"),
        A("Back to settings", href="/settings", cls="btn btn-primary btn-sm mt-4"),
        cls="p-6 space-y-2",
    )


@ar("/payments/cancel", methods=["GET"])
def payment_cancel():
    return Div(
        H2("Payment canceled"),
        P("No money was added to your account."),
        A("Back to settings", href="/settings", cls="btn btn-outline btn-sm mt-4"),
        cls="p-6 space-y-2",
    )
