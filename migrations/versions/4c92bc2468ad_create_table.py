"""create table

Revision ID: 4c92bc2468ad
Revises:
Create Date: 2024-12-07 13:05:18.749715

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

from dto import SingleUserDataDto

# revision identifiers, used by Alembic.
revision: str = "4c92bc2468ad"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    table = op.create_table(
        "data",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(250), nullable=False),
        sa.Column("first_name", sa.String(30), nullable=False),
        sa.Column("last_name", sa.String(30)),
        sa.Column("avatar", sa.Unicode(250)),
    )

    op.bulk_insert(
        table=table,
        rows=SingleUserDataDto.get_count_users(count=10),
    )


def downgrade() -> None:
    op.drop_table("data")
