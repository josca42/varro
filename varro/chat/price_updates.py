from __future__ import annotations

from genai_prices import UpdatePrices

_update_prices: UpdatePrices | None = None


def start_price_updates() -> None:
    global _update_prices
    if _update_prices is not None:
        return
    updater = UpdatePrices(update_interval=3600)
    updater.__enter__()
    updater.wait(timeout=30)
    _update_prices = updater


def stop_price_updates() -> None:
    global _update_prices
    if _update_prices is None:
        return
    _update_prices.__exit__(None, None, None)
    _update_prices = None
