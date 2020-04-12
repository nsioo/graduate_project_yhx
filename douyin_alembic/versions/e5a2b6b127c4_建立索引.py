"""建立索引

Revision ID: e5a2b6b127c4
Revises: ecfd6eed2da8
Create Date: 2020-03-28 11:32:40.660343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5a2b6b127c4'
down_revision = 'ecfd6eed2da8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_comments_text'), 'comments', ['text'], unique=False)
    op.create_index(op.f('ix_posts_desc'), 'posts', ['desc'], unique=False)
    op.create_index(op.f('ix_urltasks_user_id'), 'urltasks', ['user_id'], unique=False)
    op.create_index(op.f('ix_users_nickname'), 'users', ['nickname'], unique=False)
    op.create_index(op.f('ix_users_signature'), 'users', ['signature'], unique=False)
    op.create_index(op.f('ix_users_user_id'), 'users', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_user_id'), table_name='users')
    op.drop_index(op.f('ix_users_signature'), table_name='users')
    op.drop_index(op.f('ix_users_nickname'), table_name='users')
    op.drop_index(op.f('ix_urltasks_user_id'), table_name='urltasks')
    op.drop_index(op.f('ix_posts_desc'), table_name='posts')
    op.drop_index(op.f('ix_comments_text'), table_name='comments')
    # ### end Alembic commands ###
