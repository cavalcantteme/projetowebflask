"""empty message

Revision ID: b956fe03918b
Revises: 82119192706a
Create Date: 2018-12-01 22:24:03.098229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b956fe03918b'
down_revision = '82119192706a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('unit', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'unit')
    # ### end Alembic commands ###
