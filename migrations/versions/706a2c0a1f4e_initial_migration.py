"""Initial Migration

Revision ID: 706a2c0a1f4e
Revises: 0de77fcd1ba3
Create Date: 2018-05-28 18:06:56.417519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '706a2c0a1f4e'
down_revision = '0de77fcd1ba3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
