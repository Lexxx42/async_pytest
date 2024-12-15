"""Endpoints for work with users v0.4.2."""

from typing import Annotated

from fastapi import APIRouter, Header

from application.exceptions import InvalidTokenError, NotFoundError
from application.very_secret_token import FAKE_SECRET_TOKEN
from bd import Data, SessionDep
from dto import ErrorDto, GetSingleUserDto, UserData
from utility.custom_logging import logger

user_router = APIRouter()


@user_router.get(
    path="/routers/users/{user_id}",
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
