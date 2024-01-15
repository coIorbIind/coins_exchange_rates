from fastapi import FastAPI
import uvicorn

from config.settings import settings


def get_app():
    app = FastAPI()

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
