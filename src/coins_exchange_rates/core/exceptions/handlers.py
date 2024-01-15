from fastapi import Request
from fastapi.responses import JSONResponse

from core.logger import init_logger
from .base import BaseAPIException


logger = init_logger(__name__)


def exception_handler(request: Request, exception: BaseAPIException) -> JSONResponse:
    """ Exception to json """
    logger.error(exception.to_json())
    return JSONResponse(
        status_code=exception.status_code,
        content=exception.to_json()
    )


def python_exception_handler(request: Request, exception: Exception) -> JSONResponse:
    """ Exception to json """
    logger.error(exception)
    return JSONResponse(
        status_code=500,
        content={'detail': 'Error!'}
    )
