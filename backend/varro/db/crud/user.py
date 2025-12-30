from varro.db.crud.base import CrudBase
from sqlmodel import Session, select
from varro.db.models.user import User
from typing import Optional
from varro.db.db import engine
import bcrypt


class CrudUser(CrudBase[User]):
    def get_by_email(self, email: str) -> Optional[User]:
        with Session(self.engine) as session:
            stmt = select(User).where(User.email == email)
            return session.exec(stmt).one_or_none()

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

    def create_with_password(
        self, email: str, password: str, name: str | None = None
    ) -> User:
        password_hash = self.hash_password(password)
        new_user = User(email=email, password_hash=password_hash, name=name)
        return self.create(new_user)

    def authenticate(self, email: str, password: str) -> Optional[User]:
        db_user = self.get_by_email(email)
        if not db_user:
            return None
        if not db_user.password_hash:
            return None
        if not db_user.is_active:
            return None
        if not self.verify_password(password, db_user.password_hash):
            return None
        return db_user


user = CrudUser(User, engine)
