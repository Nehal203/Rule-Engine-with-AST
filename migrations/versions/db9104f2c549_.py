"""empty message

Revision ID: db9104f2c549
Revises: 
Create Date: 2024-10-24 17:43:13.960057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db9104f2c549'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rule', schema=None) as batch_op:
        batch_op.drop_column('ast_json')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rule', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ast_json', sa.TEXT(), nullable=False))

    # ### end Alembic commands ###
