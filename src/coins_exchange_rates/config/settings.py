from pydantic import Field
from pydantic_settings import BaseSettings


class UvicornSettings(BaseSettings):
    HOST: str = Field('0.0.0.0')
    PORT: int = Field(8000)
    RELOAD: bool = Field(True)


class CoingeckoSettings(BaseSettings):
    BASE_URL: str = 'https://api.coingecko.com/api/v3/'
    VS_CURRENCIES: list[str] = ['rub', 'usd']
    COINS: dict[str, str] = {
        'bitcoin': 'BTC',
        'ethereum': 'ETH',
        'tether': 'USDTERC',
    }
    ORDER: str = 'id_asc'


class Settings(BaseSettings):
    uvicorn: UvicornSettings = UvicornSettings()
    coingecko: CoingeckoSettings = CoingeckoSettings()

    LOG_FILE_PATH: str = Field('../../../logs/logs.log')
    LOG_LEVEL: str = Field('debug')


settings = Settings()
