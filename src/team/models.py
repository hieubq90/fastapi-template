from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import Column, String

from sqlmodel import Field, Relationship, SQLModel
from src.base_model import Base, default_uuid

if TYPE_CHECKING:
    from src.hero.models import Hero


class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str
    
    class Config:
        orm_mode = True


class Team(Base, TeamBase, table=True):
    __tablename__ = "teams"
    heroes: List["Hero"] = Relationship(back_populates="team")


class TeamCreate(TeamBase):
    pass


class TeamUpdate(SQLModel):
    id: Optional[str] = None
    name: Optional[str] = None
    headquarters: Optional[str] = None

