"""Added category_tag table and relationships on category and category_default

Revision ID: 2b4152f356e
Revises: 200425d3687d
Create Date: 2015-08-24 17:32:54.773807

"""

# revision identifiers, used by Alembic.
revision = '2b4152f356e'
down_revision = '200425d3687d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('default_category_tags',
    sa.Column('category_tag_id', sa.Integer(), nullable=True),
    sa.Column('category_default_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_default_id'], ['category_default.id'], ),
    sa.ForeignKeyConstraint(['category_tag_id'], ['category_tag.id'], )
    )
    op.create_table('category_tags',
    sa.Column('category_tag_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['category_tag_id'], ['category_tag.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category_tags')
    op.drop_table('default_category_tags')
    op.drop_table('category_tag')
    ### end Alembic commands ###