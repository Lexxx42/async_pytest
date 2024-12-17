"""DTO schema of GET /routers/users/{user_id} request."""

from pydantic import Field, StrictInt

from dto.generic import ReqResDto
from dto.user_creation_dto import UserCreation


class UserData(UserCreation):
    """User info."""

    id: StrictInt = Field(description="User id")


class GetSingleUserDto(ReqResDto):
    """Dto model for get single user data request."""

    data: UserData = Field(description="User info")
