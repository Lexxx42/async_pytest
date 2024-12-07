"""Endpoints."""

from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Header, HTTPException

from bd import Data, SessionDep, create_db_and_tables
from dto import GetSingleUserDto, UserData

FAKE_SECRET_TOKEN = "sun_of_the_beach"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan."""
    await create_db_and_tables()
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
        raise HTTPException(status_code=400, detail="Invalid X-Token header")

    user = await session.get(Data, user_id)

    if not user:
        raise HTTPException(status_code=404, detail=f"User with {user_id=} not found")

    return GetSingleUserDto(data=UserData.model_validate(user))
