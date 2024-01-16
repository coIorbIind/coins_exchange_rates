from datetime import datetime

import pytest

from config.settings import settings
from services.coingecko import CoingeckoService


@pytest.fixture
def coingecko_service() -> CoingeckoService:
    return CoingeckoService(config=settings.coingecko.model_dump())


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
                    'id': 'bitcoin',
                    'symbol': 'btc',
                    'name': 'Bitcoin',
                    'current_price': 3744337,
                    'last_updated': '2024-01-16T06:10:49.393Z',
                },
                {
                    'id': 'ethereum',
                    'symbol': 'eth',
                    'name': 'Ethereum',
                    'current_price': 221708,
                    'last_updated': '2024-01-16T06:10:49.393Z',
                },
                {
                    'id': 'tether',
                    'symbol': 'usdt',
                    'name': 'Tether',
                    'current_price': 87.57,
                    'last_updated': '2024-01-16T06:10:49.393Z',
                }
            ]
        ),
        'usd': CoingeckoPatchedAnswer(
            status_code=200,
            response_data=[
                {
                    'id': 'bitcoin',
                    'symbol': 'btc',
                    'name': 'Bitcoin',
                    'current_price': 42302,
                    'last_updated': '2024-01-16T06:10:49.393Z',
                },
                {
                    'id': 'ethereum',
                    'symbol': 'eth',
                    'name': 'Ethereum',
                    'current_price': 2516.51,
                    'last_updated': '2024-01-16T06:10:49.393Z',
                },
                {
                    'id': 'tether',
                    'symbol': 'usdt',
                    'name': 'Tether',
                    'current_price': 0.999875,
                    'last_updated': '2024-01-16T06:10:49.393Z',
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
        'BTC': {
            'rub': {
                'price': 3744337,
                'last_updated': datetime(2024, 1, 16, 6, 10, 49, 393000),
            },
            'usd': {
                'price': 42302,
                'last_updated': datetime(2024, 1, 16, 6, 10, 49, 393000),
            }
        },
        'ETH': {
            'rub': {
                'price': 221708,
                'last_updated': datetime(2024, 1, 16, 6, 10, 49, 393000),
            },
            'usd': {
                'price': 2516.51,
                'last_updated': datetime(2024, 1, 16, 6, 10, 49, 393000),
            }
        },
        'USDTERC': {
            'rub': {
                'price': 87.57,
                'last_updated': datetime(2024, 1, 16, 6, 10, 49, 393000),
            },
            'usd': {
                'price': 0.999875,
                'last_updated': datetime(2024, 1, 16, 6, 10, 49, 393000),
            }
        },
    }
