"""DTO schema of error response model."""

from pydantic import StrictStr

from dto.generic import ReqResDto


class ErrorDto(ReqResDto):
    """Dto model error response."""

    detail: StrictStr
