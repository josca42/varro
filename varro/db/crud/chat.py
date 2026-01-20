from __future__ import annotations

from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from varro.db.crud.base import CrudBase
from varro.db.db import engine
from varro.db.models.chat import Chat, Message


class CrudChat(CrudBase[Chat]):
    def get(self, chat_id: int | None, add_msgs: bool = False) -> Chat | None:
        if chat_id is None:
            return None
        with Session(self.engine) as session:
            query = select(Chat).where(Chat.id == chat_id)
            if add_msgs:
                query = query.options(selectinload(Chat.messages))
            return session.exec(query).first()

    def get_recent_by_user(self, user_id: int, limit: int = 10) -> list[Chat]:
        with Session(self.engine) as session:
            return session.exec(
                select(Chat)
                .where(Chat.user_id == user_id)
                .order_by(Chat.updated_at.desc())
                .limit(limit)
            ).all()


class CrudMessage(CrudBase[Message]):
    pass


chat = CrudChat(Chat, engine)
message = CrudMessage(Message, engine)
