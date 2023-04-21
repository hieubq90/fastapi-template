from sqlmodel import SQLModel
from src.models.base_model import Base


class DemoCreate(SQLModel):
    description: str


class Demo(Base, DemoCreate, table=True):
    __tablename__ = "demo"
