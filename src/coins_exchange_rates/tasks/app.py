from celery import Celery, Task
from dependency_injector.wiring import inject, Provide

from containers.container import AppContainer
from services import ExchangeRateService, CoingeckoService
from config.settings import settings
from core.logger import init_logger

logger = init_logger(__name__)


class TaskWithServices(Task):
    @inject
    def __init__(
        self,
        exchange_rate_service: ExchangeRateService = Provide[AppContainer.exchange_rate_service],
        coingecko_service: CoingeckoService = Provide[AppContainer.coingecko_service],
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.exchange_rate_service = exchange_rate_service
        self.coingecko_service = coingecko_service


container = AppContainer()
container.init_resources()
container.wire(modules=[__name__])
celery_app = Celery('tasks', broker=settings.redis.redis_url, task_cls=TaskWithServices)
celery_app.conf.task_serializer = 'json'
