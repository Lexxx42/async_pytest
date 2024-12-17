"""This is the main application module."""

from contextlib import asynccontextmanager
from subprocess import run
from typing import Any

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from application import exc_handlers, exceptions
from application.routers import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: ARG001
    """Lifespan."""
    run(["alembic", "upgrade", "head"], check=False)
    yield
    run(["alembic", "downgrade", "base"], check=False)


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.add_exception_handler(exceptions.InvalidTokenError, exc_handlers.invalid_token_exception_handler)  # type: ignore
app.add_exception_handler(exceptions.NotFoundError, exc_handlers.not_found_exception_handler)  # type: ignore
app.add_exception_handler(exceptions.ServerError, exc_handlers.server_exception_handler)  # type: ignore


def custom_openapi() -> dict[str, Any]:
    """Custom OpenAPI."""
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="async-pytest",
        version="0.4.3",
        summary="OpenAPI schema",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {"url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"}
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi  # type: ignore
