"""rename passsword_hash to password_hash

Revision ID: 78e6c0a5dd41
Revises: 1128a375f9bf
Create Date: 2026-04-24 16:38:13.700088

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel 


# revision identifiers, used by Alembic.
revision: str = '78e6c0a5dd41'
down_revision: Union[str, Sequence[str], None] = '1128a375f9bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('users', 'passsword_hash', new_column_name='password_hash')


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('users', 'password_hash', new_column_name='passsword_hash')
