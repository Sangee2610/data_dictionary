"""empty message

Revision ID: 028f0a77082a
Revises: 
Create Date: 2019-07-05 11:50:56.490368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '028f0a77082a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dataset_attribute', 'data_type_id',
               existing_type=sa.SMALLINT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dataset_attribute', 'data_type_id',
               existing_type=sa.SMALLINT(),
               nullable=True)
    # ### end Alembic commands ###
