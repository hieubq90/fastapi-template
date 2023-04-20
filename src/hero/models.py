from typing import Optional, TYPE_CHECKING
import uuid

from sqlmodel import Field, Relationship, SQLModel

from src.base_model import Base

if TYPE_CHECKING:
    from src.team.models import Team, TeamRead


class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

    team_id: Optional[uuid.UUID] = Field(default=None, foreign_key="teams.id")


class Hero(Base, HeroBase, table=True):
    __tablename__ = "heroes"
    team: Optional["Team"] = Relationship(back_populates="heroes")


class HeroRead(HeroBase):
    id: uuid.UUID


class HeroCreate(HeroBase):
    pass


class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
    team_id: Optional[uuid.UUID] = None


class HeroReadWithTeam(HeroRead):
    team: Optional["TeamRead"] = None
