"""Index file for package. Contains public interface."""

__all__ = ["app", "FAKE_SECRET_TOKEN"]

from application.application import app
from application.very_secret_token import FAKE_SECRET_TOKEN
