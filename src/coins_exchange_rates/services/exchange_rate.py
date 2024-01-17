from datetime import datetime
from typing import Iterator

from db.models import ExchangeRate
from db.crud.exchange_rate import ExchangeRateRepository
from db.schemas import ExchangeRateCreateSchema


class ExchangeRateService:
    """ Сервис для работы с репозиторием ExchangeRateRepository """
    def __init__(self, repository: ExchangeRateRepository) -> None:
        self._repository = repository

    async def get_all(self) -> Iterator[ExchangeRate]:
        """ Получение списка всех объектов модели """
        return await self._repository.get_all()

    async def get_object_by_id(self, id: int) -> ExchangeRate:
        """ Получение объекта по id, если объект не найден - 404 ошибка """
        return await self._repository.get_object_by_id(id)

    async def create(self, data: ExchangeRateCreateSchema) -> ExchangeRate:
        """ Создание объекта модели """
        return await self._repository.create(data)

    async def bulk_create(self, data: list[ExchangeRateCreateSchema]) -> list[ExchangeRate]:
        """ Создание нескольких объектов модели """
        return await self._repository.bulk_create(data)

    async def delete(self, id: int) -> None:
        """ Удаление объекта модели """
        return await self._repository.delete(id)

    async def search(
        self,
        exchangers: str = '',
        coins_from: str = '',
        coins_to: str = '',
        last_updated: datetime | None = None
    ) -> list[ExchangeRate]:
        """
        Поиск нужных курсов
        :param exchangers: биржи, по которым нужно вернуть ответ
        :param coins_from: валюты, курсы которых нужно получить
        :param coins_to: валюты, в которые нужно осуществить перевод
        :param last_updated: время послежнего обновления курса
        :return: список найденных курсов
        """
        return await self._repository.search(exchangers, coins_from, coins_to, last_updated)
