"""created tables heat_map, car and wheel

Revision ID: 59a9c71672ad
Revises: 
Create Date: 2020-05-02 09:45:39.281649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59a9c71672ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'heat_map',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('image_path', sa.Text),
        sa.Column('name', sa.Text),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'car',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('color', sa.Text),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'wheel',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('car_id', sa.Integer),
        sa.Column('status', sa.Text),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(('car_id',), ['car.id'], ),
    )


def downgrade():
    op.drop_table('heat_map')
    op.drop_table('car')
    op.drop_table('wheel')

