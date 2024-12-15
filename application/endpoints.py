"""Endpoints."""

from contextlib import asynccontextmanager
from typing import Annotated, Any

from fastapi import FastAPI, Header, Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from bd import Data, SessionDep
from dto import ErrorDto, GetSingleUserDto, UserData
from utility.custom_logging import logger

FAKE_SECRET_TOKEN = "sun_of_the_beach"


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: ARG001
    """Lifespan."""
    # work on migration RN
    # await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


def custom_openapi() -> dict[str, Any]:
    """Custom OpenAPI."""
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="async-pytest",
        version="0.4.1",
        summary="OpenAPI schema",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {"url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"}
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi  # type: ignore


class InvalidTokenError(Exception):
    """Invalid token exception."""

    def __init__(self, name: str):
        """Constructor.

        Args:
            name: name of token.
        """
        self.name = name


class NotFoundError(Exception):
    """Not found exception."""

    def __init__(self, name: str, id_: int):
        """Constructor.

        Args:
            name: name of entity.
            id_: id of entity.
        """
        self.id_ = id_
        self.name = name


@app.exception_handler(InvalidTokenError)
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


@app.exception_handler(NotFoundError)
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


@app.get(
    path="/api/users/{user_id}",
    responses={200: {"model": GetSingleUserDto}, 404: {"model": ErrorDto}, 400: {"model": ErrorDto}},
)
async def get_single_user(user_id: int, x_token: Annotated[str, Header()], session: SessionDep) -> GetSingleUserDto:
    """Get single user data.

    Args:
        user_id: user ID.
        x_token: request X-Token.
        session: bd session.
    """
    if x_token != FAKE_SECRET_TOKEN:
        logger.warning(f"Invalid X-Token header {x_token=}")
        raise InvalidTokenError(name=x_token)

    logger.debug(f"Get single user {user_id=}")
    user = await session.get(Data, user_id)  # type: ignore
    logger.debug(f"User {user=}")

    if not user:
        logger.warning(f"User with {user_id=} not found")
        raise NotFoundError(name="user", id_=user_id)

    dto = GetSingleUserDto(data=UserData.model_validate(user))
    logger.info(f"GetSingleUserDto: {dto}")
    return dto
