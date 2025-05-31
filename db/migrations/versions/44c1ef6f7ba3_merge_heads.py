"""merge heads

Revision ID: 44c1ef6f7ba3
Revises: ceab60455205, d2bb83ee3f90
Create Date: 2025-05-31 19:27:02.420351

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44c1ef6f7ba3'
down_revision: Union[str, None] = ('ceab60455205', 'd2bb83ee3f90')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
