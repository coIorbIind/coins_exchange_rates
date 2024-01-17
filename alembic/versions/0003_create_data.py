"""Create data

Revision ID: 0003
Revises: 0002
Create Date: 2024-01-17 10:41:02.343260

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0003'
down_revision: Union[str, None] = '0002'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(
        """
        INSERT INTO exchange_rate (exchanger, coin_from, coin_to, exchange_rate, time, is_actual) VALUES 
        ('coingecko', 'BTC', 'rub', 3775677, '2024-01-17 07:39:57', true),
        ('coingecko', 'ETH', 'rub', 225716, '2024-01-17 07:40:18', true),
        ('coingecko', 'USDTERC', 'rub', 88.23, '2024-01-17 07:40:12', true),
        ('coingecko', 'BTC', 'usd', 42717, '2024-01-17 07:48:34', true),
        ('coingecko', 'ETH', 'usd', 2554.62, '2024-01-17 07:48:42', true),
        ('coingecko', 'USDTERC', 'usd', 0.998874, '2024-01-17 07:45:16', true);
        """
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###