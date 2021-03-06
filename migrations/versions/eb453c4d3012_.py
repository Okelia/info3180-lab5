"""empty message

Revision ID: eb453c4d3012
Revises: 85fdb1d38b97
Create Date: 2021-03-02 21:27:48.618582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb453c4d3012'
down_revision = '85fdb1d38b97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
