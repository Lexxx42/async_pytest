"""Reader of secrets from .env file."""

from os import getenv
from typing import TypedDict

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
MayBeSte = str | None
BdCreds = TypedDict(
    "BdCreds",
    {"user": MayBeSte, "pass": MayBeSte, "host": MayBeSte, "port": MayBeSte, "name": MayBeSte},
)


def get_bd_credentials() -> BdCreds:
    """Get credentials from .env file."""
    return {
        "user": getenv("BD_USER"),
        "pass": getenv("BD_PASS"),
        "host": getenv("BD_HOST"),
        "port": getenv("BD_PORT"),
        "name": getenv("BD_NAME"),
    }
