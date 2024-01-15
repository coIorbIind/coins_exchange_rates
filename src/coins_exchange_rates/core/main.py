from fastapi import FastAPI
import uvicorn

from config.settings import settings
from core.exceptions import (
    BaseAPIException, exception_handler, python_exception_handler
)


def get_app():
    app = FastAPI()

    app.exception_handler(BaseAPIException)(exception_handler)
    app.exception_handler(Exception)(python_exception_handler)

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
