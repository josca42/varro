from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column
from typing import Optional
from sqlalchemy import DateTime, func


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str | None = None
    email: str = Field(unique=True, index=True)
    password_hash: str | None = None
    is_active: bool = Field(default=True)
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
        )
    )
