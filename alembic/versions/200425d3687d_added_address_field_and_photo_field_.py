"""Added address_field and photo_field columns to meeting table

Revision ID: 200425d3687d
Revises: 589ab4d20cc6
Create Date: 2015-08-21 13:13:32.569958

"""

# revision identifiers, used by Alembic.
revision = '200425d3687d'
down_revision = '589ab4d20cc6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meeting', sa.Column('address_field_id', sa.Integer(), nullable=True))
    op.add_column('meeting', sa.Column('telephone_field_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_telephone_field', 'meeting', 'custom_field', ['telephone_field_id'], ['id'])
    op.create_foreign_key('fk_address_field', 'meeting', 'custom_field', ['address_field_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_address_field', 'meeting', type_='foreignkey')
    op.drop_constraint('fk_telephone_field', 'meeting', type_='foreignkey')
    op.drop_column('meeting', 'telephone_field_id')
    op.drop_column('meeting', 'address_field_id')
    ### end Alembic commands ###
