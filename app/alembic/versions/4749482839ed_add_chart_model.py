"""add chart model

Revision ID: 4749482839ed
Revises: 98dfca618e69
Create Date: 2022-05-29 21:43:53.004603

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4749482839ed'
down_revision = '98dfca618e69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chart_enrolled',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('enrollment_type', sa.String(), nullable=True),
    sa.Column('mean_data', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chart_enrolled')
    # ### end Alembic commands ###