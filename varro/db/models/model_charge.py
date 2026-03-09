from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import Column, DateTime, Integer, Numeric, String, func
from sqlmodel import Field, SQLModel


class ModelCharge(SQLModel, table=True):
    __tablename__ = "model_charge"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    chat_id: int | None = Field(default=None, foreign_key="chat.id", index=True)
    turn_idx: int | None = Field(default=None, sa_column=Column(Integer, nullable=True))
    charge_type: str = Field(sa_column=Column(String, nullable=False))
    charge_key: str = Field(sa_column=Column(String, unique=True, nullable=False))
    model_name: str = Field(sa_column=Column(String, nullable=False))
    requests: int = Field(sa_column=Column(Integer, nullable=False))
    tool_calls: int = Field(sa_column=Column(Integer, nullable=False))
    input_tokens: int = Field(sa_column=Column(Integer, nullable=False))
    cache_write_tokens: int = Field(sa_column=Column(Integer, nullable=False))
    cache_read_tokens: int = Field(sa_column=Column(Integer, nullable=False))
    output_tokens: int = Field(sa_column=Column(Integer, nullable=False))
    usd_cost: Decimal = Field(sa_column=Column(Numeric(18, 8), nullable=False))
    usd_to_dkk_rate: Decimal = Field(sa_column=Column(Numeric(12, 6), nullable=False))
    amount_dkk: Decimal = Field(sa_column=Column(Numeric(12, 2), nullable=False))
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, server_default=func.now()),
    )
