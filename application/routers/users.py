"""Endpoints for work with users v0.4.3."""

from typing import Annotated

from fastapi import APIRouter, Body, Header
from sqlmodel import select

from application.exceptions import InvalidTokenError, NotFoundError, ServerError
from application.very_secret_token import FAKE_SECRET_TOKEN
from bd import Data, SessionDep
from dto import ErrorDto, GetSingleUserDto, UserCreation, UserData
from utility.custom_logging import logger

user_router = APIRouter()


@user_router.get(
    path="/routers/users/{user_id}",
    responses={200: {"model": GetSingleUserDto}, 404: {"model": ErrorDto}, 400: {"model": ErrorDto}},
    status_code=200,
)
async def get_single_user(user_id: int, x_token: Annotated[str, Header()], session: SessionDep) -> GetSingleUserDto:
    """Get single user data.

    Args:
        user_id: user ID.
        x_token: request X-Token.
        session: bd session.
    """
    if x_token != FAKE_SECRET_TOKEN:
        logger.error(f"Invalid X-Token header {x_token=}")
        raise InvalidTokenError(name=x_token)

    logger.debug(f"Get single user {user_id=}")
    user = await session.get(Data, user_id)  # type: ignore
    logger.debug(f"User {user=}")

    if not user:
        logger.error(f"User with {user_id=} not found")
        raise NotFoundError(name="user", id_=user_id)

    dto = GetSingleUserDto(data=UserData.model_validate(user))
    logger.info(f"GetSingleUserDto: {dto}")
    return dto


@user_router.post(
    path="/routers/users",
    responses={201: {"model": GetSingleUserDto}, 500: {"model": ErrorDto}},
    status_code=201,
)
async def post_add_user(
    user_data: Annotated[UserCreation, Body()],
    x_token: Annotated[str, Header()],
    session: SessionDep,
) -> GetSingleUserDto:
    """Add user.

    Args:
        user_data: user creation data.
        x_token: request X-Token.
        session: bd session.
    """
    if x_token != FAKE_SECRET_TOKEN:
        logger.warning(f"Invalid X-Token header {x_token=}")
        raise InvalidTokenError(name=x_token)

    logger.debug(f"Adding user {user_data=}")

    new_user = Data(
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        avatar=user_data.avatar,
    )

    try:
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        logger.debug(f"User added {new_user=}")

        q = select(Data).order_by(-Data.id)  # type: ignore
        result = await session.execute(q)
        act_res = result.first()[0]
        logger.debug(f"Result {act_res}")

    except Exception:
        raise ServerError(name="Server error see logs")

    dto = GetSingleUserDto(data=UserData.model_validate(act_res))
    logger.info(f"GetSingleUserDto: {dto}")
    return dto
