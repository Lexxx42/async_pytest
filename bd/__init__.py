"""Index file for package. Contains public interface."""

__all__ = ["get_session", "create_db_and_tables", "Data", "SessionDep"]

from bd.bd import SessionDep, create_db_and_tables, get_session
from bd.models import Data
