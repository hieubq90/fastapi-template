from sqlmodel import SQLModel

from src.base_model import Base


class DemoCreate(SQLModel):
    description: str


# class DemoBase()


class Demo(Base, DemoCreate, table=True):
    pass
