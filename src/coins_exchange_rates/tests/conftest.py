import pytest
from fastapi.testclient import TestClient

from core.main import get_app

from .fixtures.coingecko import coingecko_service, coingecko_valid_answer, coingecko_invalid_answer, coingecko_result


@pytest.fixture(scope='session')
def client():
    app = get_app()
    return TestClient(app)
