"""empty message

Revision ID: cb7a2162d8b7
Revises: 07c3056cd75c
Create Date: 2023-07-04 18:41:07.859695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb7a2162d8b7'
down_revision = '07c3056cd75c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('like', sa.Column('like', sa.Boolean(), nullable=True))
    op.drop_column('like', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('like', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('like', 'like')
    # ### end Alembic commands ###