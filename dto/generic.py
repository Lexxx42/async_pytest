"""Module contains parent class for validation schemas."""

from pydantic import BaseModel, ConfigDict


class ReqResDto(BaseModel):
    """Base class for schemas."""

    model_config = ConfigDict(extra="forbid", from_attributes=True)
