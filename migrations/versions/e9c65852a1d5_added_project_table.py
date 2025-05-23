"""Added Project table

Revision ID: e9c65852a1d5
Revises: 2be5431ef8c8
Create Date: 2025-05-13 15:36:58.313474

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9c65852a1d5'
down_revision: Union[str, None] = '2be5431ef8c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('start_date', sa.String(length=25), nullable=False),
    sa.Column('end_date', sa.String(length=25), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_projects_id'), 'projects', ['id'], unique=False)
    op.add_column('darbuotojai', sa.Column('project_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'darbuotojai', 'projects', ['project_id'], ['id'])
    op.add_column('employers', sa.Column('project_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'employers', 'projects', ['project_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employers', type_='foreignkey')
    op.drop_column('employers', 'project_id')
    op.drop_constraint(None, 'darbuotojai', type_='foreignkey')
    op.drop_column('darbuotojai', 'project_id')
    op.drop_index(op.f('ix_projects_id'), table_name='projects')
    op.drop_table('projects')
    # ### end Alembic commands ###
