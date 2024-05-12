""" Module contains parent class for validation schemas. """
from pydantic import BaseModel, ConfigDict


class ReqResDto(BaseModel):
    """ Base class for Reqres schemas. """
    model_config = ConfigDict(extra='forbid')
