"""Add group id to user table

Revision ID: 6f0b5fd3b44e
Revises: 92cae7ab3f0f
Create Date: 2023-11-20 22:03:25.960441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6f0b5fd3b44e"
down_revision: Union[str, None] = "92cae7ab3f0f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("group_id", sa.UUID(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "group_id")
    # ### end Alembic commands ###