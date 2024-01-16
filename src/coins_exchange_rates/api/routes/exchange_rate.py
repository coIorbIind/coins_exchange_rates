from collections import defaultdict

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from api.schemas import ExchangerSchema, CourseSchema
from containers.container import AppContainer
from db.schemas import ExchangeRateGetSchema
from services import ExchangeRateService

router = APIRouter()


@router.get(path='/courses',)
@inject
async def courses(
    exchangers: str = '',
    coins_from: str = '',
    coins_to: str = '',
    exchange_rate_service: ExchangeRateService = Depends(Provide[AppContainer.exchange_rate_service]),
) -> list[ExchangerSchema]:
    stored_courses = await exchange_rate_service.search(exchangers, coins_from, coins_to)

    response = defaultdict(list)
    for exchange_rate in stored_courses:
        pair = f'{exchange_rate.coin_from.upper()}-{exchange_rate.coin_to.upper()}'
        response[exchange_rate.exchanger].append(
            CourseSchema(direction=pair, value=exchange_rate.exchange_rate)
        )
    return [
        ExchangerSchema(exchanger=exchanger, courses=exchanger_courses)
        for exchanger, exchanger_courses in response.items()
    ]
