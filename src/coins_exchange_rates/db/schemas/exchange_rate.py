from typing import Optional
from decimal import Decimal
from datetime import datetime

from .base import BaseModelSchema


class ExchangeRateBaseSchema(BaseModelSchema):
    exchanger: str
    coin_from: str
    coin_to: str
    exchange_rate: Decimal
    time: datetime
    is_actual: bool


class ExchangeRateGetSchema(ExchangeRateBaseSchema):
    id: int


class ExchangeRateCreateSchema(ExchangeRateBaseSchema):
    pass
