from datetime import datetime
from decimal import Decimal
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from typing import Optional
from sqlalchemy import DateTime, Numeric, func, text


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str | None = None
    email: str = Field(unique=True, index=True)
    password_hash: str | None = None
    is_active: bool = Field(default=True)
    balance: Decimal = Field(
        default=Decimal("0.00"),
        sa_column=Column(Numeric(12, 2), nullable=False, server_default=text("0.00")),
    )
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime, server_default=func.now())
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now())
    )
