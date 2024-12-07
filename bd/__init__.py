"""Index file for package. Contains public interface."""

__all__ = ["get_session", "Data", "SessionDep", "DB_URL"]

from bd.bd import SessionDep, get_session, DB_URL
from bd.models import Data
