# Stripe payments + user balance

Implemented Stripe top-up flow for account balance with DKK-only amounts.

- `user.balance` added as `NUMERIC(12,2)` with default `0.00`.
- New `stripe_payment` table stores paid checkout sessions and Stripe event IDs.
- Webhook path: `POST /payments/webhook` verifies `STRIPE_WEBHOOK_SECRET`.
- Idempotency: webhook checks existing `checkout_session_id` or `stripe_event_id` before crediting.
- Crediting rule: on `checkout.session.completed` with `payment_status=paid`, increment `user.balance` by `amount_total/100`.
- Refund events are ignored in app (no balance reversal in v1).
- Checkout path: `POST /payments/checkout` creates Stripe Checkout session in `dkk` using dynamic `price_data`.
- User pages:
  - `GET /payments/success?checkout_sid=...` shows credited amount or pending state.
  - `GET /payments/cancel` shows cancellation state.
  - Settings page now shows balance and top-up controls (`50/100/200` presets + custom amount).

Required env keys:

- `STRIPE_SECRET_KEY`
- `STRIPE_WEBHOOK_SECRET`
