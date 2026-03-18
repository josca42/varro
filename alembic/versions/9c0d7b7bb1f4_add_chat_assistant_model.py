"""Add chat assistant model.

Revision ID: 9c0d7b7bb1f4
Revises: 2f4d88a72f0d
Create Date: 2026-03-13 13:30:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "9c0d7b7bb1f4"
down_revision: Union[str, None] = "2f4d88a72f0d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "chat",
        sa.Column(
            "assistant_model",
            sa.String(),
            nullable=False,
            server_default="anthropic_opus",
        ),
    )
    op.alter_column("chat", "assistant_model", server_default=None)


def downgrade() -> None:
    op.drop_column("chat", "assistant_model")
