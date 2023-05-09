"""change ticker to ticker_symbol

Revision ID: f181f2be01c3
Revises: 31e490833160
Create Date: 2023-05-08 13:34:43.325976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f181f2be01c3'
down_revision = '31e490833160'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('monthly_transaction_ffm',
    sa.Column('monthly_transaction_ffm_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('market_minus_risk_free', sa.Float(), nullable=True),
    sa.Column('small_minus_big', sa.Float(), nullable=True),
    sa.Column('high_minus_low', sa.Float(), nullable=True),
    sa.Column('risk_free', sa.Float(), nullable=True),
    sa.Column('market_rate', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('monthly_transaction_ffm_id')
    )
    with op.batch_alter_table('monthly_transaction_ffm', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_monthly_transaction_ffm_date'), ['date'], unique=False)
        batch_op.create_index(batch_op.f('ix_monthly_transaction_ffm_high_minus_low'), ['high_minus_low'], unique=False)
        batch_op.create_index(batch_op.f('ix_monthly_transaction_ffm_market_minus_risk_free'), ['market_minus_risk_free'], unique=False)
        batch_op.create_index(batch_op.f('ix_monthly_transaction_ffm_market_rate'), ['market_rate'], unique=False)
        batch_op.create_index(batch_op.f('ix_monthly_transaction_ffm_risk_free'), ['risk_free'], unique=False)
        batch_op.create_index(batch_op.f('ix_monthly_transaction_ffm_small_minus_big'), ['small_minus_big'], unique=False)

    op.create_table('ticker',
    sa.Column('permno', sa.Integer(), nullable=False),
    sa.Column('ticker_symbol', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('permno')
    )
    with op.batch_alter_table('ticker', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_ticker_ticker_symbol'), ['ticker_symbol'], unique=False)

    op.create_table('monthly_transaction',
    sa.Column('monthly_transaction_id', sa.Integer(), nullable=False),
    sa.Column('permno', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('share_type', sa.String(), nullable=True),
    sa.Column('exchange', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('returns', sa.Float(), nullable=True),
    sa.Column('shares_outstanding', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['permno'], ['ticker.permno'], ),
    sa.PrimaryKeyConstraint('monthly_transaction_id'),
    sa.UniqueConstraint('permno', 'date')
    )
    with op.batch_alter_table('monthly_transaction', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_monthly_transaction_date'), ['date'], unique=False)
        batch_op.create_index(batch_op.f('ix_monthly_transaction_exchange'), ['exchange'], unique=False)
        batch_op.create_index(batch_op.f('ix_monthly_transaction_permno'), ['permno'], unique=False)
        batch_op.create_index(batch_op.f('ix_monthly_transaction_price'), ['price'], unique=False)
        batch_op.create_index(batch_op.f('ix_monthly_transaction_returns'), ['returns'], unique=False)
        batch_op.create_index(batch_op.f('ix_monthly_transaction_share_type'), ['share_type'], unique=False)
        batch_op.create_index(batch_op.f('ix_monthly_transaction_shares_outstanding'), ['shares_outstanding'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('monthly_transaction', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_monthly_transaction_shares_outstanding'))
        batch_op.drop_index(batch_op.f('ix_monthly_transaction_share_type'))
        batch_op.drop_index(batch_op.f('ix_monthly_transaction_returns'))
        batch_op.drop_index(batch_op.f('ix_monthly_transaction_price'))
        batch_op.drop_index(batch_op.f('ix_monthly_transaction_permno'))
        batch_op.drop_index(batch_op.f('ix_monthly_transaction_exchange'))
        batch_op.drop_index(batch_op.f('ix_monthly_transaction_date'))

    op.drop_table('monthly_transaction')
    with op.batch_alter_table('ticker', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_ticker_ticker_symbol'))

    op.drop_table('ticker')
    with op.batch_alter_table('monthly_transaction_ffm', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_monthly_transaction_ffm_small_minus_big'))
        batch_op.drop_index(batch_op.f('ix_monthly_transaction_ffm_risk_free'))
        batch_op.drop_index(batch_op.f('ix_monthly_transaction_ffm_market_rate'))
        batch_op.drop_index(batch_op.f('ix_monthly_transaction_ffm_market_minus_risk_free'))
        batch_op.drop_index(batch_op.f('ix_monthly_transaction_ffm_high_minus_low'))
        batch_op.drop_index(batch_op.f('ix_monthly_transaction_ffm_date'))

    op.drop_table('monthly_transaction_ffm')
    # ### end Alembic commands ###