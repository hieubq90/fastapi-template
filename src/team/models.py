from typing import List, Optional, TYPE_CHECKING
import uuid

from sqlmodel import Field, Relationship, SQLModel
from src.base_model import Base

if TYPE_CHECKING:
    from src.hero.models import Hero, HeroRead


class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str


class Team(Base, TeamBase, table=True):
    __tablename__ = "teams"
    heroes: List["Hero"] = Relationship(back_populates="team")


class TeamCreate(TeamBase):
    pass


class TeamRead(TeamBase):
    id: uuid.UUID


class TeamUpdate(SQLModel):
    id: Optional[uuid.UUID] = None
    name: Optional[str] = None
    headquarters: Optional[str] = None


class TeamReadWithHeroes(TeamRead):
    heroes: List["HeroRead"] = []
