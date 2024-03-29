"""empty message

Revision ID: 8fb3329d560f
Revises: 5fe9766be8b0
Create Date: 2017-12-18 22:26:14.617908

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8fb3329d560f'
down_revision = '5fe9766be8b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.drop_column('question', 'creat_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('creat_time', mysql.DATETIME(), nullable=True))
    op.drop_column('question', 'create_time')
    # ### end Alembic commands ###
