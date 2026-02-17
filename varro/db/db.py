from varro.config import settings
from sqlmodel import SQLModel, create_engine, Session

POSTGRES_SQLALCHEMY_URI = f"postgresql+psycopg://{settings['DBUSER']}:{settings['DBPASS']}@localhost:5432/neocortex"
POSTGRES_DSN = (
    f"postgresql://{settings['DBUSER']}:{settings['DBPASS']}@localhost:5432/neocortex"
)

engine = create_engine(POSTGRES_SQLALCHEMY_URI)
