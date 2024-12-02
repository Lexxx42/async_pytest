"""Database models."""

from sqlmodel import Field, SQLModel


class Data(SQLModel, table=True):
    __tablename__ = "data"

    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(index=True)
    first_name: str
    last_name: str
    avatar: str
