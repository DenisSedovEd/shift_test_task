"""fix next_raise_datesalary colomn in user tables

Revision ID: 9f76cf87273f
Revises: 5f7384ff1af2
Create Date: 2025-07-01 16:26:50.951261

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9f76cf87273f"
down_revision: Union[str, Sequence[str], None] = "5f7384ff1af2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "salaries", sa.Column("next_raise_date", sa.DateTime(), nullable=False)
    )
    op.drop_column("salaries", "next_raise_data")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "salaries", sa.Column("next_raise_data", sa.DATETIME(), nullable=False)
    )
    op.drop_column("salaries", "next_raise_date")
