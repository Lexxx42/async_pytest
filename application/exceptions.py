"""Custom exceptions."""


class InvalidTokenError(Exception):
    """Invalid token exception."""

    def __init__(self, name: str):
        """Constructor.

        Args:
            name: name of token.
        """
        self.name = name


class NotFoundError(Exception):
    """Not found exception."""

    def __init__(self, name: str, id_: int):
        """Constructor.

        Args:
            name: name of entity.
            id_: id of entity.
        """
        self.id_ = id_
        self.name = name
