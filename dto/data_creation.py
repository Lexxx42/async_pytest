"""DTO for DB data creation."""

from typing import Self

from pydantic import EmailStr, StrictStr

from dto.generic import ReqResDto
from randoms.data_generator import get_random_avatar_url, get_random_email, get_random_fullname


class SingleUserDataDto(ReqResDto):
    """User info for creation."""

    email: EmailStr
    first_name: StrictStr
    last_name: StrictStr
    avatar: StrictStr

    @classmethod
    def create_random(cls) -> Self:
        """Create random user info."""
        f_name, l_name = get_random_fullname()

        return cls(
            email=get_random_email(),
            first_name=f_name,
            last_name=l_name,
            avatar=get_random_avatar_url(),
        )

    @classmethod
    def get_count_users(cls, count: int = 10) -> list[dict[str, str]]:
        """Get count random users.

        Args:
            count: count of users.
        """
        return [cls.create_random().model_dump(mode='json') for _ in range(count)]
