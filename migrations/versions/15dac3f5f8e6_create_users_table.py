"""Create users table

Revision ID: 15dac3f5f8e6
Revises: 
Create Date: 2019-09-11 19:28:54.058808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15dac3f5f8e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(80), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('users')
