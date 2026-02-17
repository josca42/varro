from varro.db.crud.base import CrudBase
from sqlmodel import Session, select
from varro.db.models.user import User
from typing import Optional
from varro.db.db import engine
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from varro.agent.workspace import ensure_user_workspace

hasher = PasswordHasher()


class CrudUser(CrudBase[User]):
    def create(self, obj: User) -> User:
        created = super().create(obj)
        if created.id is not None:
            ensure_user_workspace(created.id)
        return created

    def get_by_email(self, email: str) -> Optional[User]:
        with Session(self.engine) as session:
            stmt = select(User).where(User.email == email)
            return session.exec(stmt).one_or_none()

    @staticmethod
    def hash_password(password: str) -> str:
        return hasher.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        if not hashed_password.startswith("$argon2"):
            return False
        try:
            return hasher.verify(hashed_password, plain_password)
        except VerifyMismatchError:
            return False

    def create_with_password(
        self,
        email: str,
        password: str,
        name: str | None = None,
        is_active: bool = True,
    ) -> User:
        password_hash = self.hash_password(password)
        new_user = User(
            email=email,
            password_hash=password_hash,
            name=name,
            is_active=is_active,
        )
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
