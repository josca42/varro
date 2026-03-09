# Model cost debiting from user balance

Added prepaid model billing wired into chat runtime.

- New ledger table: `model_charge`.
- One debit is recorded per user chat run with idempotency key `assistant:{run_id}`.
- Debit is based on `RunUsage` token fields, including Anthropic cache token fields.
- Cost source: `genai_prices.calc_price(usage, model_name)` in USD.
- Conversion to DKK uses fixed env rate: `MODEL_COST_USD_TO_DKK_RATE`.
- DKK debit amount is rounded to 2 decimals before balance update.
- Debit persistence and balance decrement happen in one transaction.
- Low balance gate: chat run start is blocked when `user.balance <= 0`.
- Failed assistant runs are still debited if usage exists.
- Title generation (`claude-haiku-4-5`) is also debited with key `title:{chat_id}:{turn_idx}`.
- `genai-prices` updater now runs continuously in app lifecycle (`UpdatePrices`), refreshing hourly.
