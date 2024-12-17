"""DTO body for POST /routers/users request."""

from pydantic import EmailStr, Field, StrictStr

from dto.generic import ReqResDto


class UserCreation(ReqResDto):
    """User creation info."""

    email: EmailStr = Field(description="User email")
    first_name: StrictStr = Field(description="User first name")
    last_name: StrictStr = Field(description="User last name")
    avatar: StrictStr = Field(default="template_avatar.png", description="User avatar URL")
