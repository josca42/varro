from varro.config import settings
from sqlmodel import SQLModel, create_engine, Session

POSTGRES_USER_SQLALCHEMY = f"postgresql+psycopg://{settings['USEROWNER_USER']}:{settings['USEROWNER_PASS']}@localhost:5432/user"
POSTGRES_DST = (
    f"postgresql://{settings['DSTOWNER_USER']}:{settings['DSTOWNER_PASS']}@localhost:5432/dst"
)

dst_read_engine = create_engine(f"postgresql+psycopg://{settings['DSTREAD_USER']}:{settings['DSTREAD_PASS']}@localhost:5432/dst")
dst_owner_engine = create_engine(f"postgresql+psycopg://{settings['DSTOWNER_USER']}:{settings['DSTOWNER_PASS']}@localhost:5432/dst")
user_engine = create_engine(f"postgresql+psycopg://{settings['USEROWNER_USER']}:{settings['USEROWNER_PASS']}@localhost:5432/user")
engine = create_engine(POSTGRES_USER_SQLALCHEMY)
