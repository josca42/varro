"""Add model charge table.

Revision ID: 2f4d88a72f0d
Revises: 8e6f7f3900f0
Create Date: 2026-03-09 10:15:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "2f4d88a72f0d"
down_revision: Union[str, None] = "8e6f7f3900f0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "model_charge",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("chat_id", sa.Integer(), nullable=True),
        sa.Column("turn_idx", sa.Integer(), nullable=True),
        sa.Column("charge_type", sa.String(), nullable=False),
        sa.Column("charge_key", sa.String(), nullable=False),
        sa.Column("model_name", sa.String(), nullable=False),
        sa.Column("requests", sa.Integer(), nullable=False),
        sa.Column("tool_calls", sa.Integer(), nullable=False),
        sa.Column("input_tokens", sa.Integer(), nullable=False),
        sa.Column("cache_write_tokens", sa.Integer(), nullable=False),
        sa.Column("cache_read_tokens", sa.Integer(), nullable=False),
        sa.Column("output_tokens", sa.Integer(), nullable=False),
        sa.Column("usd_cost", sa.Numeric(precision=18, scale=8), nullable=False),
        sa.Column("usd_to_dkk_rate", sa.Numeric(precision=12, scale=6), nullable=False),
        sa.Column("amount_dkk", sa.Numeric(precision=12, scale=2), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["chat_id"], ["chat.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("charge_key"),
    )
    op.create_index(
        op.f("ix_model_charge_user_id"),
        "model_charge",
        ["user_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_model_charge_chat_id"),
        "model_charge",
        ["chat_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_model_charge_chat_id"), table_name="model_charge")
    op.drop_index(op.f("ix_model_charge_user_id"), table_name="model_charge")
    op.drop_table("model_charge")
