"""DTO schema of error response model."""

from pydantic import Field, StrictInt, StrictStr

from dto.generic import ReqResDto


class ErrorDto(ReqResDto):
    """Dto model error response."""

    detail: StrictStr = Field(description="Error message")
    status_code: StrictInt = Field(description="HTTP status code")
