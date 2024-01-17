from dependency_injector import containers, providers

from config.settings import settings
from db.database import Database
from db.crud.exchange_rate import ExchangeRateRepository
from services import ExchangeRateService, CoingeckoService


class AppContainer(containers.DeclarativeContainer):
    """ DI контейнер для работы с сервисами """
    config = providers.Configuration()
    config.from_dict(settings.model_dump())

    db = providers.Singleton(Database)

    exchange_rate_repository = providers.Singleton(
        ExchangeRateRepository,
        session_factory=db.provided.session
    )
    exchange_rate_service = providers.Factory(
        ExchangeRateService,
        repository=exchange_rate_repository,
    )
    coingecko_service = providers.Factory(CoingeckoService, config=config.coingecko)
