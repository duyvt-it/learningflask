"""Tao Bang User

Revision ID: eee73960fc23
Revises: fcb089a1780f
Create Date: 2021-01-19 00:57:31.997034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eee73960fc23'
down_revision = 'fcb089a1780f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('body', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'body')
    # ### end Alembic commands ###