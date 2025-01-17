"""增加urltask表

Revision ID: 25e835bc50c4
Revises: c445b38dc52a
Create Date: 2020-03-16 15:58:38.911162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25e835bc50c4'
down_revision = 'c445b38dc52a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urltasks',
    sa.Column('url', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=50), nullable=True),
    sa.Column('analyse_count', sa.Integer(), server_default=sa.text('0'), nullable=False),
    sa.Column('updateTime', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('createTime', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False),
    sa.PrimaryKeyConstraint('url'),
    mysql_charset='utf8mb4'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('urltasks')
    # ### end Alembic commands ###
