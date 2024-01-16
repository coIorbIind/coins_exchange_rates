from fastapi import FastAPI
import uvicorn

from api.routes import exchange_rate
from config.settings import settings
from containers.container import AppContainer
from core.exceptions import (
    BaseAPIException, exception_handler, python_exception_handler
)


def get_app():
    container = AppContainer()
    container.config.from_dict(settings.model_dump())
    container.wire(modules=[exchange_rate])

    app = FastAPI()

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
