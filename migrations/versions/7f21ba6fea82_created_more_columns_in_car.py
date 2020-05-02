"""created more columns in car

Revision ID: 7f21ba6fea82
Revises: 59a9c71672ad
Create Date: 2020-05-02 10:01:10.579419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f21ba6fea82'
down_revision = '59a9c71672ad'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('car', sa.Column('fuel', sa.Text))
    op.add_column('car', sa.Column('power', sa.Text))
    op.add_column('car', sa.Column('speed', sa.Text))
    op.add_column('car', sa.Column('avg_consume', sa.Text))


def downgrade():
    op.drop_column('car', 'fuel')
    op.drop_column('car', 'power')
    op.drop_column('car', 'speed')
    op.drop_column('car', 'avg_consume')
