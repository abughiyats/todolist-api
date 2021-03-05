"""add ondelete=cascade on project_id

Revision ID: 9c21790a68cb
Revises: 9cdbd4aaad86
Create Date: 2021-03-06 01:19:13.392354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c21790a68cb'
down_revision = '9cdbd4aaad86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('task_ibfk_1', 'task', type_='foreignkey')
    op.create_foreign_key(None, 'task', 'project', ['project_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.create_foreign_key('task_ibfk_1', 'task', 'project', ['project_id'], ['id'])
    # ### end Alembic commands ###
