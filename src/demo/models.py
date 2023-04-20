from sqlalchemy import Column, String
from sqlmodel import Field, SQLModel

from src.base_model import Base, default_uuid


class DemoCreate(SQLModel):
    description: str


class Demo(Base, DemoCreate, table=True):
    __tablename__ = "demo"

    # id: str = Field(
    #     primary_key=True,
    #     sa_column=Column(String(), primary_key=True, default=default_uuid),
    # )
