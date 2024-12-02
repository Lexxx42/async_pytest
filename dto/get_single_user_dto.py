"""DTO schema of GET /api/users/{user_id} request."""

from pydantic import EmailStr, StrictInt, StrictStr

from dto.generic import ReqResDto


class UserData(ReqResDto):
    """User info."""

    id: StrictInt
    email: EmailStr
    first_name: StrictStr
    last_name: StrictStr
    avatar: StrictStr


class GetSingleUserDto(ReqResDto):
    """Dto model for get single user data request."""

    data: UserData
