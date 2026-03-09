from __future__ import annotations

from decimal import Decimal
from types import SimpleNamespace

from pydantic_ai.usage import RunUsage

from varro.chat import model_costs


def test_apply_model_charge_returns_none_when_no_usage(monkeypatch) -> None:
    called = {"value": False}

    def fake_create(_charge):
        called["value"] = True
        return True

    monkeypatch.setattr(model_costs.crud.model_charge, "create_and_debit_balance", fake_create)

    result = model_costs.apply_model_charge(
        user_id=1,
        chat_id=2,
        turn_idx=3,
        charge_type="assistant_run",
        charge_key="assistant:run-1",
        model_name="claude-opus-4-6",
        usage=RunUsage(),
    )

    assert result is None
    assert called["value"] is False


def test_apply_model_charge_builds_ledger_row(monkeypatch) -> None:
    captured = {}

    monkeypatch.setattr(
        model_costs,
        "calc_price",
        lambda _usage, _model_name: SimpleNamespace(total_price=0.123456),
    )
    monkeypatch.setattr(model_costs, "usd_to_dkk_rate", lambda: Decimal("7.5"))

    def fake_create(charge):
        captured["charge"] = charge
        return True

    monkeypatch.setattr(model_costs.crud.model_charge, "create_and_debit_balance", fake_create)

    result = model_costs.apply_model_charge(
        user_id=7,
        chat_id=11,
        turn_idx=0,
        charge_type="assistant_run",
        charge_key="assistant:run-abc",
        model_name="claude-opus-4-6",
        usage=RunUsage(
            requests=2,
            tool_calls=3,
            input_tokens=1000,
            cache_write_tokens=400,
            cache_read_tokens=100,
            output_tokens=250,
        ),
    )

    assert result is not None
    assert result.applied is True
    assert result.usd_cost == Decimal("0.123456")
    assert result.amount_dkk == Decimal("0.93")
    assert captured["charge"].charge_key == "assistant:run-abc"
    assert captured["charge"].charge_type == "assistant_run"
    assert captured["charge"].model_name == "claude-opus-4-6"
    assert captured["charge"].requests == 2
    assert captured["charge"].tool_calls == 3
    assert captured["charge"].input_tokens == 1000
    assert captured["charge"].cache_write_tokens == 400
    assert captured["charge"].cache_read_tokens == 100
    assert captured["charge"].output_tokens == 250
    assert captured["charge"].usd_cost == Decimal("0.123456")
    assert captured["charge"].amount_dkk == Decimal("0.93")
