"""create salary table

Revision ID: 9528bc2fd440
Revises: 172940d9d3da
Create Date: 2025-07-01 12:49:17.863602

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9528bc2fd440"
down_revision: Union[str, Sequence[str], None] = "172940d9d3da"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "salaries",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("next_raise_data", sa.DateTime(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_salaries_user_id_users")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_salaries")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("salaries")
