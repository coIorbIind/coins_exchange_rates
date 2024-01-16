import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from api.routes import exchange_rate
from config.settings import settings
from containers.container import AppContainer
from core.exceptions import (
    BaseAPIException, exception_handler, python_exception_handler
)
from tasks import coingecko


def get_app():
    container = AppContainer()
    container.config.from_dict(settings.model_dump())
    container.wire(modules=[exchange_rate, coingecko])

    app = FastAPI()

    @app.on_event('startup')
    async def startup():
        redis = aioredis.from_url(settings.redis.redis_url, encoding='utf8', decode_responses=True)
        FastAPICache.init(RedisBackend(redis), prefix='api:cache')

    app.exception_handler(BaseAPIException)(exception_handler)
    app.exception_handler(Exception)(python_exception_handler)

    app.include_router(exchange_rate.router, prefix='/api/v1', tags=['courses'])

    return app


if __name__ == '__main__':
    uvicorn.run(
        'asgi:app',
        reload=settings.uvicorn.RELOAD,
        host=settings.uvicorn.HOST,
        port=settings.uvicorn.PORT,
        log_level=settings.LOG_LEVEL,
        http='h11',
        loop='asyncio',
    )
