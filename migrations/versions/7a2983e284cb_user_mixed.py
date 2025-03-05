"""User mixed

Revision ID: 7a2983e284cb
Revises: 0a11586eb377
Create Date: 2025-03-04 17:05:12.264286

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a2983e284cb'
down_revision: Union[str, None] = '0a11586eb377'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_deleted', sa.Boolean(), nullable=False, server_default=sa.false()))
    op.add_column('users', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'deleted_at')
    op.drop_column('users', 'is_deleted')
    # ### end Alembic commands ###
