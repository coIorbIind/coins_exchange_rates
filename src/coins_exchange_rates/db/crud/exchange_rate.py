from datetime import datetime
from typing import Callable, Iterator
from contextlib import AbstractContextManager

from sqlalchemy import func
from sqlalchemy.orm import Session

from db.models import ExchangeRate
from db.schemas import ExchangeRateCreateSchema
from core.exceptions import ObjectNotFound
from core.logger import init_logger


logger = init_logger(__name__)


class ExchangeRateRepository:
    order = (ExchangeRate.time, )

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    async def get_all(self) -> Iterator[ExchangeRate]:
        """ Получение списка всех объектов модели """
        with self.session_factory() as session:
            return session.query(ExchangeRate).all().order_by(*self.order)

    async def get_object_by_id(self, id: int) -> ExchangeRate:
        """ Получение объекта по id, если объект не найден - 404 ошибка """
        with self.session_factory() as session:
            exchange_rate = session.query(ExchangeRate).filter(ExchangeRate.id == id).first()
            if not exchange_rate:
                raise ObjectNotFound
            return exchange_rate

    async def create(self, data: ExchangeRateCreateSchema) -> ExchangeRate:
        """ Создание объекта модели """
        with self.session_factory() as session:
            exchange_rate = ExchangeRate(**data.model_dump())
            session.add(exchange_rate)
            session.commit()
            session.refresh(exchange_rate)
            logger.info(
                f'Create new object for pair {exchange_rate.coin_from}-{exchange_rate.coin_to}'
                f' in {exchange_rate.exchanger}'
            )
            return exchange_rate

    async def bulk_create(self, data: list[ExchangeRateCreateSchema]) -> list[ExchangeRate]:
        """ Создание нескольких объектов модели """
        objs = [ExchangeRate(**obj.model_dump()) for obj in data]
        if objs:
            with self.session_factory() as session:
                old_objs = session.query(ExchangeRate).filter(ExchangeRate.exchanger == objs[0].exchanger)
                if old_objs:
                    for old_obj in old_objs:
                        old_obj.is_actual = False
                    session.add_all(old_objs)
                session.add_all(objs)
                session.commit()
                logger.info(
                    f'Create new {len(objs)} object for pair in {objs[0].exchanger}'
                )
                for obj in objs:
                    session.refresh(obj)
        return objs

    async def delete(self, id: int) -> None:
        """ Удаление объекта модели """
        with self.session_factory() as session:
            obj = await self.get_object_by_id(id=id)
            session.delete(obj)
            session.commit()
        return

    async def search(
        self,
        exchangers: str = '',
        coins_from: str = '',
        coins_to: str = '',
        last_updated: datetime | None = None
    ):
        filters = self._get_filters(exchangers, coins_from, coins_to)
        if last_updated:
            filters.append(ExchangeRate.time == last_updated)

        with self.session_factory() as session:
            return session.query(ExchangeRate).filter(*filters).order_by(*self.order)

    def _get_filters(self, exchangers: str = '', coins_from: str = '', coins_to: str = '') -> list:
        filters = [ExchangeRate.is_actual.is_(True)]
        if exchangers:
            exchangers = [exchanger.lower().strip() for exchanger in exchangers.split(',')]
            filters.append(func.lower(ExchangeRate.exchanger).in_(exchangers))
        if coins_from:
            coins_from = [coin_from.lower().strip() for coin_from in coins_from.split(',')]
            filters.append(func.lower(ExchangeRate.coin_from).in_(coins_from))
        if coins_to:
            coins_to = [coin_to.lower().strip() for coin_to in coins_to.split(',')]
            filters.append(func.lower(ExchangeRate.coin_to).in_(coins_to))
        return filters
