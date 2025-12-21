from sqlalchemy import text
from varro.db.db import engine


def get_dim_tables() -> tuple[str, ...]:
    with engine.connect() as conn:
        return tuple(
            row[0]
            for row in conn.execute(
                text(
                    "SELECT table_name FROM information_schema.tables WHERE table_schema = 'dim'"
                )
            )
        )
