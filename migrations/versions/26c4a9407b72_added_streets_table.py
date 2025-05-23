"""Added Streets table

Revision ID: 26c4a9407b72
Revises: a99203e0f124
Create Date: 2025-05-13 16:57:26.693781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26c4a9407b72'
down_revision: Union[str, None] = 'a99203e0f124'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('streets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_streets_id'), 'streets', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_streets_id'), table_name='streets')
    op.drop_table('streets')
    # ### end Alembic commands ###
