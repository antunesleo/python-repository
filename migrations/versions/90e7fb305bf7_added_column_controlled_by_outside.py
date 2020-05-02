"""added column controlled by outside

Revision ID: 90e7fb305bf7
Revises: 7f21ba6fea82
Create Date: 2020-05-02 10:25:59.066820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90e7fb305bf7'
down_revision = '7f21ba6fea82'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('car', sa.Column('controlled_outside', sa.Text))


def downgrade():
    op.drop_column('car', 'controlled_outside')
