from fastapi import APIRouter, Depends

from dependency_injector.wiring import inject, Provide

from containers.container import AppContainer
from services import ExchangeRateService
from db.schemas import ExchangeRateGetSchema


router = APIRouter()


@router.get(path='/courses',)
@inject
async def courses(
    exchange_rate_service: ExchangeRateService = Depends(Provide[AppContainer.exchange_rate_service]),
) -> list[ExchangeRateGetSchema]:
    return await exchange_rate_service.get_all()
