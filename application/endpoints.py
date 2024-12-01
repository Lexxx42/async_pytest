"""Endpoints."""
from typing import Annotated

from fastapi import FastAPI, Header, HTTPException

from application.fake_db import USER_INFO_DB
from dto import get_single_user_dto as single_user

FAKE_SECRET_TOKEN = "sun_of_the_beach"
app = FastAPI()


@app.get(path="/api/users/{user_id}", response_model=single_user.GetSingleUserDto)
async def get_single_user(user_id: int, x_token: Annotated[str, Header()]):
    """Get single user data.

    Args:
        user_id: user ID.
        x_token: request X-Token.
    """
    if x_token != FAKE_SECRET_TOKEN:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")

    if (result := USER_INFO_DB.get(user_id)) is None:
        raise HTTPException(status_code=404, detail=f"User with {user_id=} not found")

    return result
