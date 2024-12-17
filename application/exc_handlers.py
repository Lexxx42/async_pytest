"""Exception Handlers."""

from fastapi import Request
from fastapi.responses import JSONResponse

from application.exceptions import InvalidTokenError, NotFoundError, ServerError
from dto import ErrorDto


async def invalid_token_exception_handler(request: Request, exc: InvalidTokenError) -> JSONResponse:  # noqa: ARG001
    """Invalid token exception handler.

    Args:
        request: request.
        exc: exception.
    """
    code = 400
    return JSONResponse(
        status_code=code,
        content=ErrorDto(status_code=code, detail=f"Invalid {exc.name} token").model_dump(mode="json"),
    )


async def not_found_exception_handler(request: Request, exc: NotFoundError) -> JSONResponse:  # noqa: ARG001
    """Not found exception handler.

    Args:
        request: request.
        exc: exception.
    """
    code = 404
    return JSONResponse(
        status_code=code,
        content=ErrorDto(status_code=code, detail=f"{exc.name} with id={exc.id_} not found").model_dump(mode="json"),
    )


async def server_exception_handler(request: Request, exc: ServerError) -> JSONResponse:  # noqa: ARG001
    """Server exception handler.

    Args:
        request: request.
        exc: exception.
    """
    code = 500
    return JSONResponse(
        status_code=code,
        content=ErrorDto(status_code=code, detail=exc.name).model_dump(mode="json"),
    )
