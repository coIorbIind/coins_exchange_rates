from typing import Callable, Iterator
from contextlib import AbstractContextManager

from sqlalchemy.orm import Session

from db.models import ExchangeRate
from db.schemas import ExchangeRateCreateSchema
from core.exceptions import ObjectNotFound


class ExchangeRateRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    async def get_all(self) -> Iterator[ExchangeRate]:
        """ Получение списка всех объектов модели """
        with self.session_factory() as session:
            return session.query(ExchangeRate).all()

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
            return exchange_rate

    async def delete(self, id: int) -> None:
        """ Удаление объекта модели """
        obj = await self.get_object_by_id(id=id)
        await obj.delete()
        return
