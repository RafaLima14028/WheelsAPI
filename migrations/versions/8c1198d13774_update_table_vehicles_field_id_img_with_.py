"""Update table vehicles, field id_img with null

Revision ID: 8c1198d13774
Revises: 3f1dd0361cc1
Create Date: 2025-04-12 15:55:09.454681

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c1198d13774'
down_revision: Union[str, None] = '3f1dd0361cc1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        table_name='vehicles',
        column_name='id_img',
        existing_type=sa.ARRAY(sa.Integer),
        nullable=True
    )


def downgrade() -> None:
    op.alter_column(
        table_name='vehicles',
        column_name='id_img',
        existing_type=sa.ARRAY(sa.Integer),
        nullable=False
    )
