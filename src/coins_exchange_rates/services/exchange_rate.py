from typing import Iterator

from db.models import ExchangeRate
from db.crud.exchange_rate import ExchangeRateRepository
from db.schemas import ExchangeRateCreateSchema


class ExchangeRateService:

    def __init__(self, repository: ExchangeRateRepository) -> None:
        self._repository = repository

    async def get_all(self) -> Iterator[ExchangeRate]:
        return await self._repository.get_all()

    async def get_object_by_id(self, id: int) -> ExchangeRate:
        return await self._repository.get_object_by_id(id)

    async def create(self, data: ExchangeRateCreateSchema) -> ExchangeRate:
        return await self._repository.create(data)

    async def delete(self, id: int) -> None:
        return await self._repository.delete(id)
