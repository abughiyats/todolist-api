"""add relationship

Revision ID: 9f924964606a
Revises: 9c21790a68cb
Create Date: 2021-03-06 04:56:36.328204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f924964606a'
down_revision = '9c21790a68cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'project', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'project', type_='foreignkey')
    op.drop_column('project', 'user_id')
    # ### end Alembic commands ###