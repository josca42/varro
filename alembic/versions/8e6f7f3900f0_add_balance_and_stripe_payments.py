"""Add user balance and stripe payments.

Revision ID: 8e6f7f3900f0
Revises: 3a93fe8a91c0
Create Date: 2026-03-08 09:10:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "8e6f7f3900f0"
down_revision: Union[str, None] = "3a93fe8a91c0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "user",
        sa.Column(
            "balance",
            sa.Numeric(precision=12, scale=2),
            server_default=sa.text("0.00"),
            nullable=False,
        ),
    )

    op.create_table(
        "stripe_payment",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("checkout_session_id", sa.String(), nullable=False),
        sa.Column("stripe_event_id", sa.String(), nullable=False),
        sa.Column("payment_intent_id", sa.String(), nullable=True),
        sa.Column("amount_dkk", sa.Numeric(precision=12, scale=2), nullable=False),
        sa.Column("currency", sa.String(), nullable=False),
        sa.Column("payment_status", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("checkout_session_id"),
        sa.UniqueConstraint("stripe_event_id"),
    )
    op.create_index(op.f("ix_stripe_payment_user_id"), "stripe_payment", ["user_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_stripe_payment_user_id"), table_name="stripe_payment")
    op.drop_table("stripe_payment")
    op.drop_column("user", "balance")
