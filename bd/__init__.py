"""Index file for package. Contains public interface."""

__all__ = ["get_session", "Data", "SessionDep", "DB_URL"]

from bd.bd import DB_URL, SessionDep, get_session
from bd.models import Data
