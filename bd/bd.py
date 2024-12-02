"""Database."""

from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

from utility.secret_reader import get_bd_credentials

bd_creds = get_bd_credentials()
user = bd_creds["user"]
passwd = bd_creds["pass"]
host = bd_creds["host"]
port = bd_creds["port"]
name = bd_creds["name"]

engine = create_engine(url=f"postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{name}", echo=True)


def create_db_and_tables():
    """BD initialization."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Session initialization."""
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
