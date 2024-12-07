"""Database."""

from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, SQLModel, create_engine

from utility.secret_reader import get_bd_credentials

bd_creds = get_bd_credentials()
user = bd_creds["user"]
passwd = bd_creds["pass"]
host = bd_creds["host"]
port = bd_creds["port"]
name = bd_creds["name"]

engine = create_async_engine(url=f"postgresql+asyncpg://{user}:{passwd}@{host}:{port}/{name}", echo=True, future=True)


async def create_db_and_tables():
    """BD initialization."""
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Session initialization."""
    async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
