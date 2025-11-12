from varro.db.crud.base import CrudBase
from sqlmodel import SQLModel, Session, select
from varro.db.models.user import User
from typing import Optional
from varro.db.db import engine


class CrudUser(CrudBase[User]):
    def get_by_email(self, email: str) -> Optional[User]:
        with Session(self.engine) as session:
            stmt = select(User).where(User.email == email)
            return session.exec(stmt).one_or_none()


user = CrudUser(User, engine)
