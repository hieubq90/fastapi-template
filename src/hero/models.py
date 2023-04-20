from typing import Optional, TYPE_CHECKING
from sqlalchemy import Column, String
from sqlmodel import Field, Relationship, SQLModel
from src.base_model import Base, default_uuid

# if TYPE_CHECKING:
from src.team.models import Team


class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

    team_id: Optional[str] = Field(default=None, foreign_key="teams.id")
    
    class Config:
        orm_mode = True


class Hero(Base, HeroBase, table=True):
    __tablename__ = "heroes"
    
    team: Optional[Team] = Relationship(back_populates="heroes")


class HeroCreate(HeroBase):
    pass


class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
    team_id: Optional[str] = None

