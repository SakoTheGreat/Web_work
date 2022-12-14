"""users and news tables

Revision ID: 8365c011f7b2
Revises: 9bf05d16ad88
Create Date: 2022-10-28 23:02:33.534876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8365c011f7b2'
down_revision = '9bf05d16ad88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
