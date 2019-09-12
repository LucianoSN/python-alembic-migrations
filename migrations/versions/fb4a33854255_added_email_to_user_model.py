"""Added email to User model

Revision ID: fb4a33854255
Revises: 67d4f207606b
Create Date: 2019-09-12 00:19:16.170265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb4a33854255'
down_revision = '67d4f207606b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=50), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.drop_index('ix_users_name', table_name='users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_users_name', 'users', ['name'], unique=False)
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
