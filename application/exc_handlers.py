"""Exception Handlers."""

from fastapi import Request
from fastapi.responses import JSONResponse

from application.exceptions import InvalidTokenError, NotFoundError
from dto import ErrorDto


async def invalid_token_exception_handler(request: Request, exc: InvalidTokenError) -> JSONResponse:  # noqa: ARG001
    """Invalid token exception handler.

    Args:
        request: request.
        exc: exception.
    """
    return JSONResponse(
        status_code=400,
        content=ErrorDto(status_code=400, detail=f"Invalid {exc.name} token").model_dump(mode="json"),
    )


async def not_found_exception_handler(request: Request, exc: NotFoundError) -> JSONResponse:  # noqa: ARG001
    """Not found exception handler.

    Args:
        request: request.
        exc: exception.
    """
    return JSONResponse(
        status_code=404,
        content=ErrorDto(status_code=404, detail=f"{exc.name} with id={exc.id_} not found").model_dump(mode="json"),
    )
