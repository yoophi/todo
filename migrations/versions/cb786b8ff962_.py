"""empty message

Revision ID: cb786b8ff962
Revises: 2bd2b430f3a3
Create Date: 2016-01-29 23:23:03.149477

"""

# revision identifiers, used by Alembic.
revision = 'cb786b8ff962'
down_revision = '2bd2b430f3a3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('is_completed', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    ### end Alembic commands ###
