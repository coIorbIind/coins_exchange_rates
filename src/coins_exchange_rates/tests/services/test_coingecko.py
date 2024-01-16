import pytest
from unittest.mock import patch


@pytest.mark.parametrize('is_response_valid', [True, False])
def test_get_exchange_rates(
    coingecko_service, coingecko_valid_answer, coingecko_invalid_answer, coingecko_result, is_response_valid
):
    def patched_response(url, *args, **kwargs):
        if is_response_valid:
            answer = coingecko_valid_answer
        else:
            answer = coingecko_invalid_answer
        if 'rub' in url:
            return answer['rub']
        return answer['usd']

    with patch('requests.get', patched_response):
        exchange_rates = coingecko_service.get_exchange_rates()
    if is_response_valid:
        assert exchange_rates == coingecko_result
    else:
        assert exchange_rates == {}
