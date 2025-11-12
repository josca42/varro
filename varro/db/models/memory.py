from __future__ import annotations
import io
import mimetypes
import unicodedata
from pathlib import Path
from typing import Optional, List
from sqlmodel import Session, select, delete
from sqlalchemy import UniqueConstraint, func, update
from minio import Minio
from minio.error import S3Error
from mojo.db.crud.base import CrudBase
from mojo.db.models.file import File, MemoryFile
from mojo.db.db import engine, minio_client
from sqlalchemy.dialects.postgresql import insert

SYSTEM_USER_ID = 15


class CrudMemoryFile:
    """
    Focused CRUD for MemoryFile using SQLModel/SQLAlchemy.
    Postgres upsert is used for create/overwrite.
    All operations are scoped to: (user_id == self.user_id) OR (user_id == SYSTEM_USER_ID).
    """

    def __init__(self, engine, user_id: int):
        self.engine = engine
        self.user_id = user_id

    def _visible(self):
        return MemoryFile.user_id.in_([self.user_id, SYSTEM_USER_ID])

    def get_by_path(self, path: str) -> Optional[MemoryFile]:
        with Session(self.engine) as session:
            return session.exec(
                select(MemoryFile).where(MemoryFile.path == path, self._visible())
            ).one_or_none()

    def list_paths_under_prefix(self, prefix: str) -> list[str]:
        with Session(self.engine) as session:
            like_prefix = prefix.rstrip("/") + "/%"
            q = select(MemoryFile.path).where(
                (MemoryFile.path == prefix) | (MemoryFile.path.like(like_prefix)),
                self._visible(),
            )
            return session.exec(q).all()

    def upsert_file(
        self, path: str, file_text: str, user_id: int | None = None
    ) -> MemoryFile:
        user_id = user_id if user_id else self.user_id
        with Session(self.engine) as session, session.begin():
            stmt = (
                insert(MemoryFile)
                .values(path=path, file_text=file_text, user_id=user_id)
                .on_conflict_do_update(
                    index_elements=[MemoryFile.path, MemoryFile.user_id],
                    set_={"file_text": file_text, "updated_at": func.now()},
                )
                .returning(MemoryFile)
            )
            obj = session.exec(stmt).scalar_one_or_none()
            return obj

    # ---- Update text ----
    def set_text(self, path: str, new_text: str) -> Optional[MemoryFile]:
        with Session(self.engine) as session, session.begin():
            stmt = (
                update(MemoryFile)
                .where(MemoryFile.path == path, MemoryFile.user_id == self.user_id)
                .values(file_text=new_text, updated_at=func.now())
                .returning(MemoryFile)
            )
            return session.exec(stmt).scalar_one_or_none()

    # ---- Delete ----
    def delete_file(self, path: str) -> int:
        with Session(self.engine) as session, session.begin():
            obj = session.exec(
                select(MemoryFile).where(
                    (MemoryFile.path == path), (MemoryFile.user_id == self.user_id)
                )
            ).one_or_none()
            if obj is None:
                return 0
            session.delete(obj)
            return 1

    # ---- Rename ----
    def rename_file(self, old_path: str, new_path: str) -> bool:
        with Session(self.engine) as session, session.begin():
            # Keep this global to respect the unique constraint on path
            if session.exec(
                select(MemoryFile).where(MemoryFile.path == new_path)
            ).one_or_none():
                raise ValueError(f"Target already exists: {new_path}")

            stmt = (
                update(MemoryFile)
                .where(MemoryFile.path == old_path, MemoryFile.user_id == self.user_id)
                .values(path=new_path, updated_at=func.now())
                .returning(MemoryFile)
            )
            updated = session.exec(stmt).scalar_one_or_none()
            return updated is not None

    def delete_all_system_files(self) -> int:
        with Session(self.engine) as session, session.begin():
            stmt = delete(MemoryFile).where(MemoryFile.user_id == SYSTEM_USER_ID)
            return session.exec(stmt).rowcount
