from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import Column, DateTime, Numeric, String, func
from sqlmodel import Field, SQLModel


class StripePayment(SQLModel, table=True):
    __tablename__ = "stripe_payment"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    checkout_session_id: str = Field(sa_column=Column(String, unique=True, nullable=False))
    stripe_event_id: str = Field(sa_column=Column(String, unique=True))
    payment_intent_id: str | None = None
    amount_dkk: Decimal = Field(sa_column=Column(Numeric(12, 2), nullable=False))
    currency: str = Field(sa_column=Column(String, nullable=False))
    payment_status: str = Field(sa_column=Column(String, nullable=False))
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, server_default=func.now()),
    )
