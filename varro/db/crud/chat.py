from __future__ import annotations

from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from varro.db.crud.base import CrudBase
from varro.db.db import engine
from varro.db.models.chat import Chat, Message
from pydantic_ai.messages import ModelMessagesTypeAdapter


class CrudChat(CrudBase[Chat]):
    def __init__(self, model, engine, user_id: int | None = None):
        super().__init__(model, engine)
        self._user_id = user_id

    def for_user(self, user_id: int) -> CrudChat:
        """Return a copy scoped to this user."""
        return CrudChat(self.model, self.engine, user_id)

    def _apply_user_filter(self, query):
        """Add user_id filter if set."""
        if self._user_id is not None:
            query = query.where(Chat.user_id == self._user_id)
        return query

    def get(self, chat_id: int | None, with_msgs: bool = False) -> Chat | None:
        if chat_id is None:
            return None
        with Session(self.engine) as session:
            query = select(Chat).where(Chat.id == chat_id)
            query = self._apply_user_filter(query)
            if with_msgs:
                query = query.options(selectinload(Chat.messages))
            chat = session.exec(query).first()
            if with_msgs:
                chat.messages = ModelMessagesTypeAdapter.validate_python(chat.messages)
            return chat

    def get_recent(self, limit: int = 10) -> list[Chat]:
        with Session(self.engine) as session:
            query = select(Chat).order_by(Chat.updated_at.desc()).limit(limit)
            query = self._apply_user_filter(query)
            return session.exec(query).all()


class CrudMessage(CrudBase[Message]): ...


chat = CrudChat(Chat, engine)
message = CrudMessage(Message, engine)
