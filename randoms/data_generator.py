"""Random data generation module."""

from random import choice

from mimesis import Internet, Person
from mimesis.enums import Gender
from mimesis.locales import Locale

from utility.custom_logging import logger


def get_random_fullname(locale: Locale = Locale.RU) -> tuple[str, str]:
    """Generate random fullname.

    Args:
        locale: Locale to use.
    """
    person = Person(locale=locale)
    gender = choice(list(Gender))

    full_name = person.full_name(gender=gender)
    name, last_name = full_name.split()
    logger.debug(f"Generated random fullname: {name=}, {last_name=}")

    return name, last_name


def get_random_email(locale: Locale = Locale.RU) -> str:
    """Generate random email.

    Args:
        locale: Locale to use.
    """
    person = Person(locale=locale)

    email = person.email()
    logger.debug(f"Generated random email: {email=}")

    return email


def get_random_avatar_url() -> str:
    """Generate random avatar url."""
    internet = Internet()
    url = f"{internet.uri()}/avatar.png"
    logger.debug(f"Generated random avatar url: {url=}")

    return url
