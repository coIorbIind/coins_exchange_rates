import asyncio

from db.schemas import ExchangeRateCreateSchema


from core.logger import init_logger
from .app import celery_app, TaskWithServices


logger = init_logger(__name__)


@celery_app.task(bind=True)
def coingecko_periodic_task(self: TaskWithServices):
    new_data = self.coingecko_service.get_exchange_rates()
    logger.info('Get data from coingecko')

    objs_to_create = []
    for coin, coin_data in new_data.items():
        for currency, currency_data in coin_data.items():
            objs_to_create.append(
                ExchangeRateCreateSchema(
                    exchanger='coingecko',
                    coin_from=coin,
                    coin_to=currency.upper(),
                    exchange_rate=currency_data['price'],
                    time=currency_data['last_updated'],
                )
            )
    res = asyncio.run(self.exchange_rate_service.bulk_create(objs_to_create))
    for obj in res:
        print(obj.id)
