from varro.config import settings
from sqlmodel import SQLModel, create_engine, Session

POSTGRES_SQLALCHEMY_URI = f"postgresql+psycopg://{settings['DBUSER']}:{settings['DBPASS']}@localhost:5432/neocortex"
POSTGRES_DSN = (
    f"postgresql://{settings['DBUSER']}:{settings['DBPASS']}@localhost:5432/neocortex"
)
ASYNC_DSN = f"postgresql+asyncpg://{settings['DBUSER']}:{settings['DBPASS']}@localhost:5432/neocortex"
CHAINLIT_DSN = f"postgresql+asyncpg://{settings['DBUSER']}:{settings['DBPASS']}@localhost:5432/chainlit"

engine = create_engine(POSTGRES_SQLALCHEMY_URI)
