import pytest

from config.settings import settings
from services.coingecko import CoingeckoService


@pytest.fixture
def coingecko_service() -> CoingeckoService:
    return CoingeckoService(config=settings.coingecko)


class CoingeckoPatchedAnswer:
    def __init__(self, status_code: int, response_data: list[dict] | dict):
        self.status_code = status_code
        self.text = str(response_data)
        self.data = response_data

    def json(self):
        return self.data


@pytest.fixture
def coingecko_valid_answer():
    return {
        'rub': CoingeckoPatchedAnswer(
            status_code=200,
            response_data=[
                {
                    "id": "bitcoin",
                    "symbol": "btc",
                    "name": "Bitcoin",
                    "current_price": 3744337,
                },
                {
                    "id": "ethereum",
                    "symbol": "eth",
                    "name": "Ethereum",
                    "current_price": 221708,
                },
                {
                    "id": "tether",
                    "symbol": "usdt",
                    "name": "Tether",
                    "current_price": 87.57,
                }
            ]
        ),
        'usd': CoingeckoPatchedAnswer(
            status_code=200,
            response_data=[
                {
                    "id": "bitcoin",
                    "symbol": "btc",
                    "name": "Bitcoin",
                    "current_price": 42302,
                },
                {
                    "id": "ethereum",
                    "symbol": "eth",
                    "name": "Ethereum",
                    "current_price": 2516.51,
                },
                {
                    "id": "tether",
                    "symbol": "usdt",
                    "name": "Tether",
                    "current_price": 0.999875,
                }
            ]
        )
    }


@pytest.fixture
def coingecko_invalid_answer():
    return {
        'rub': CoingeckoPatchedAnswer(
            status_code=504,
            response_data={'error': 'timeout_error'}
        ),
        'usd': CoingeckoPatchedAnswer(
            status_code=500,
            response_data={'error': 'server_error'}
        )
    }


@pytest.fixture
def coingecko_result():
    return {
        'BTC': {'rub': 3744337, 'usd': 42302},
        'ETH': {'rub': 221708, 'usd': 2516.51},
        'USDTERC': {'rub': 87.57, 'usd': 0.999875},
    }
