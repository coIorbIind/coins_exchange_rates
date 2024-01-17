from collections import defaultdict

from fastapi import APIRouter, Depends
from fastapi_cache import JsonCoder
from fastapi_cache.decorator import cache
from dependency_injector.wiring import inject, Provide

from api.schemas import ExchangerSchema, CourseSchema
from containers.container import AppContainer
from services import ExchangeRateService
from utils.cache import key_builder

router = APIRouter()


@router.get(path='/courses')
@inject
@cache(expire=5, coder=JsonCoder, key_builder=key_builder)
async def courses(
    exchangers: str = '',
    coins_from: str = '',
    coins_to: str = '',
    exchange_rate_service: ExchangeRateService = Depends(Provide[AppContainer.exchange_rate_service]),
) -> list[ExchangerSchema]:
    """
    Endpoint для получения актуальных курсов валют с бирж
    :param exchangers: биржи, по которым нужно вернуть ответ
    :param coins_from: валюты, курсы которых нужно получить
    :param coins_to: валюты, в которые нужно осуществить перевод
    :param exchange_rate_service: DI сервис для общения с репозиторием
    :return: список курсов сгруппированных по бирже
    """
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
