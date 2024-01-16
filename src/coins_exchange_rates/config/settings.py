from pydantic import Field
from pydantic_settings import BaseSettings


class UvicornSettings(BaseSettings):
    HOST: str = Field('0.0.0.0')
    PORT: int = Field(8000)
    RELOAD: bool = Field(True)


class DBSettings(BaseSettings):
    DB_HOST: str = Field('localhost')
    DB_PORT: str = Field('5433')
    DB_NAME: str = Field('coins')
    DB_USER: str = Field('postgres')
    DB_PASSWORD: str = Field('postgres')

    @property
    def database_url(self) -> str:
        return f'postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


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
    db: DBSettings = DBSettings()

    LOG_FILE_PATH: str = Field('../../../logs/logs.log')
    LOG_LEVEL: str = Field('debug')


settings = Settings()
