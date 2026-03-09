from __future__ import annotations

import os
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

from genai_prices import calc_price
from pydantic_ai.usage import RunUsage

from varro.config import settings
from varro.db import crud
from varro.db.models.model_charge import ModelCharge

DKK_AMOUNT_QUANT = Decimal("0.01")


@dataclass
class ModelChargeResult:
    applied: bool
    charge_key: str
    model_name: str
    usd_cost: Decimal
    amount_dkk: Decimal


def config_value(key: str) -> str | None:
    return settings.get(key) or os.environ.get(key)


def usd_to_dkk_rate() -> Decimal:
    value = config_value("MODEL_COST_USD_TO_DKK_RATE")
    if not value:
        raise RuntimeError("MODEL_COST_USD_TO_DKK_RATE is required.")
    return Decimal(str(value))


def has_usage(usage: RunUsage) -> bool:
    return any(
        (
            usage.requests,
            usage.input_tokens,
            usage.cache_write_tokens,
            usage.cache_read_tokens,
            usage.output_tokens,
        )
    )


def has_positive_balance(user_id: int) -> bool:
    user = crud.user.get(user_id)
    if not user:
        raise RuntimeError(f"User not found for billing: {user_id}")
    return user.balance > 0


def apply_model_charge(
    *,
    user_id: int,
    chat_id: int | None,
    turn_idx: int | None,
    charge_type: str,
    charge_key: str,
    model_name: str,
    usage: RunUsage,
) -> ModelChargeResult | None:
    if not has_usage(usage):
        return None

    price = calc_price(usage, model_name)
    usd_cost = Decimal(str(price.total_price))
    rate = usd_to_dkk_rate()
    amount_dkk = (usd_cost * rate).quantize(DKK_AMOUNT_QUANT, rounding=ROUND_HALF_UP)

    charge = ModelCharge(
        user_id=user_id,
        chat_id=chat_id,
        turn_idx=turn_idx,
        charge_type=charge_type,
        charge_key=charge_key,
        model_name=model_name,
        requests=int(usage.requests or 0),
        tool_calls=int(usage.tool_calls or 0),
        input_tokens=int(usage.input_tokens or 0),
        cache_write_tokens=int(usage.cache_write_tokens or 0),
        cache_read_tokens=int(usage.cache_read_tokens or 0),
        output_tokens=int(usage.output_tokens or 0),
        usd_cost=usd_cost,
        usd_to_dkk_rate=rate,
        amount_dkk=amount_dkk,
    )
    applied = crud.model_charge.create_and_debit_balance(charge)
    return ModelChargeResult(
        applied=applied,
        charge_key=charge_key,
        model_name=model_name,
        usd_cost=usd_cost,
        amount_dkk=amount_dkk,
    )
