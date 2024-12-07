"""Endpoints."""

from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Header, HTTPException

from bd import Data, SessionDep
from dto import GetSingleUserDto, UserData
from utility.custom_logging import logger

FAKE_SECRET_TOKEN = "sun_of_the_beach"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan."""
    # work on migration RN
    # await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get(path="/api/users/{user_id}", response_model=GetSingleUserDto)
async def get_single_user(user_id: int, x_token: Annotated[str, Header()], session: SessionDep) -> GetSingleUserDto:
    """Get single user data.

    Args:
        user_id: user ID.
        x_token: request X-Token.
        session: bd session.
    """
    if x_token != FAKE_SECRET_TOKEN:
        logger.warning(f"Invalid X-Token header {x_token=}")
        raise HTTPException(status_code=400, detail="Invalid X-Token header")

    logger.debug(f"Get single user {user_id=}")
    user = await session.get(Data, user_id)
    logger.debug(f"User {user=}")

    if not user:
        logger.warning(f"User with {user_id=} not found")
        raise HTTPException(status_code=404, detail=f"User with {user_id=} not found")

    dto = GetSingleUserDto(data=UserData.model_validate(user))
    logger.info(f"GetSingleUserDto: {dto}")
    return dto
