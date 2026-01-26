from __future__ import annotations

from pathlib import Path

from sqlalchemy.orm import selectinload
from sqlmodel import Session, select, delete

from varro.db.crud.base import CrudBase
from varro.db.db import engine
from varro.db.models.chat import Chat, Turn


class CrudChat(CrudBase[Chat]):
    def __init__(self, model, engine, user_id: int | None = None):
        super().__init__(model, engine)
        self._user_id = user_id

    def for_user(self, user_id: int) -> CrudChat:
        return CrudChat(self.model, self.engine, user_id)

    def _apply_user_filter(self, query):
        if self._user_id is not None:
            query = query.where(Chat.user_id == self._user_id)
        return query

    def create(self, chat: Chat) -> Chat:
        if self._user_id is not None:
            chat.user_id = self._user_id
        return super().create(chat)

    def get(self, chat_id: int | None, with_turns: bool = False) -> Chat | None:
        if chat_id is None:
            return None
        with Session(self.engine) as session:
            query = select(Chat).where(Chat.id == chat_id)
            query = self._apply_user_filter(query)
            if with_turns:
                query = query.options(selectinload(Chat.turns))
            return session.exec(query).first()

    def get_recent(self, limit: int = 10) -> list[Chat]:
        with Session(self.engine) as session:
            query = select(Chat).order_by(Chat.updated_at.desc()).limit(limit)
            query = self._apply_user_filter(query)
            return list(session.exec(query).all())


class CrudTurn(CrudBase[Turn]):
    def delete_from_idx(self, chat_id: int, idx: int) -> list[str]:
        """
        Delete all turns with idx >= given idx.
        Returns list of obj_fp paths that were deleted (for file cleanup).
        """
        with Session(self.engine) as session:
            query = select(Turn).where(
                Turn.chat_id == chat_id,
                Turn.idx >= idx,
            )
            to_delete = list(session.exec(query).all())
            deleted_paths = [t.obj_fp for t in to_delete]

            stmt = delete(Turn).where(
                Turn.chat_id == chat_id,
                Turn.idx >= idx,
            )
            session.exec(stmt)
            session.commit()

            return deleted_paths


chat = CrudChat(Chat, engine)
turn = CrudTurn(Turn, engine)
