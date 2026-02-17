from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, Relationship, SQLModel


class Chat(SQLModel, table=True):
    """A chat conversation containing multiple turns."""

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    title: str | None = None
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, server_default=func.now()),
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()),
    )
    turns: list["Turn"] = Relationship(
        back_populates="chat",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "order_by": "Turn.idx",
        },
    )


class Turn(SQLModel, table=True):
    """A single turn in a chat conversation (user prompt + assistant response)."""

    id: Optional[int] = Field(default=None, primary_key=True)
    chat_id: int = Field(foreign_key="chat.id", index=True)
    user_text: str
    obj_fp: str
    idx: int
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, server_default=func.now()),
    )
    chat: Chat | None = Relationship(back_populates="turns")
