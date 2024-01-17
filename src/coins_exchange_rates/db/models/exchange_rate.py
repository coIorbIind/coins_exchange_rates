import sqlalchemy as sa

from ..database import Base


class ExchangeRate(Base):
    """ Модель для хранения информации о курсах валют """
    __tablename__ = 'exchange_rate'
    id = sa.Column(sa.Integer, name='id', primary_key=True, autoincrement=True)
    exchanger = sa.Column(sa.String, name='exchanger', index=True)
    coin_from = sa.Column(sa.String, name='coin_from')
    coin_to = sa.Column(sa.String, name='coin_to')
    exchange_rate = sa.Column(sa.DECIMAL, name='exchange_rate')
    is_actual = sa.Column(sa.Boolean, name='is_actual', nullable=True, default=False)
    time = sa.Column(sa.DateTime, name='time')
