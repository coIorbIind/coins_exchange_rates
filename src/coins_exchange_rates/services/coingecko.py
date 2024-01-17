from collections import defaultdict
from datetime import datetime

import requests

from config.settings import CoingeckoSettings
from core.logger import init_logger


logger = init_logger(__name__)


class CoingeckoService:
    """ Сервис для работы с CoingeckoAPI """
    def __init__(self, config: CoingeckoSettings):
        self.base_url = config['BASE_URL']
        self.vs_currencies = config['VS_CURRENCIES']
        self.coins = config['COINS']
        self.order = config['ORDER']

    def get_exchange_rates(self) -> dict[str, dict[str, float]]:
        """ Получение списка курсов через CoingeckoAPI """
        result = defaultdict(dict)

        for vs_currency in self.vs_currencies:
            url = (
                f'{self.base_url}coins/markets?'
                f'vs_currency={vs_currency}'
                f'&ids={",".join(self.coins)}'
                f'&order={self.order}'
            )
            response = requests.get(url)
            if response.status_code != 200:
                logger.error(f'Get {response.status_code} status code from coingecko with data: "{response.text}"')
                continue

            for coin_data in response.json():
                result[self.coins[coin_data['id']]][vs_currency] = {}
                result[self.coins[coin_data['id']]][vs_currency]['price'] = coin_data['current_price']
                result[self.coins[coin_data['id']]][vs_currency]['last_updated'] = datetime.fromisoformat(
                    coin_data['last_updated'][:-1]
                )

        return result
