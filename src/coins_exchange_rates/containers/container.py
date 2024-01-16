from dependency_injector import containers, providers

from db.database import Database
from db.crud.exchange_rate import ExchangeRateRepository
from services.exchange_rate import ExchangeRateService


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    db = providers.Singleton(Database)

    exchange_rate_repository = providers.Singleton(
        ExchangeRateRepository,
        session_factory=db.provided.session
    )
    exchange_rate_service = providers.Factory(
        ExchangeRateService,
        repository=exchange_rate_repository,
    )
