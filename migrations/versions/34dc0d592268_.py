"""empty message

Revision ID: 34dc0d592268
Revises: 8cb05e7cf1d8
Create Date: 2016-01-28 11:32:43.278758

"""

# revision identifiers, used by Alembic.
revision = '34dc0d592268'
down_revision = '8cb05e7cf1d8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('current_login_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'current_login_at')
    ### end Alembic commands ###
