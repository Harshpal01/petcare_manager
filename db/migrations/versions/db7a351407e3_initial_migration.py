"""Initial migration

Revision ID: db7a351407e3
Revises: 
Create Date: 2025-05-29 12:19:29.386468

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'db7a351407e3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
