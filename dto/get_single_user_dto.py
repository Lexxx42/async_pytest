"""DTO schema of GET /routers/users/{user_id} request."""

from pydantic import EmailStr, Field, StrictInt, StrictStr

from dto.generic import ReqResDto


class UserData(ReqResDto):
    """User info."""

    id: StrictInt = Field(description="User id")
    email: EmailStr = Field(description="User email")
    first_name: StrictStr = Field(description="User first name")
    last_name: StrictStr = Field(description="User last name")
    avatar: StrictStr = Field(description="User avatar URL")


class GetSingleUserDto(ReqResDto):
    """Dto model for get single user data request."""

    data: UserData = Field(description="User info")
