from pydantic import Field
from pydantic_settings import BaseSettings


class UvicornSettings(BaseSettings):
    HOST: str = Field('0.0.0.0')
    PORT: int = Field(8000)
    RELOAD: bool = Field(True)


class Settings(BaseSettings):
    uvicorn: UvicornSettings = UvicornSettings()

    LOG_FILE_PATH: str = Field('../../../logs/logs.log')
    LOG_LEVEL: str = Field('debug')


settings = Settings()
