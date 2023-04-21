# Import all the models, so that Base has them before being
# imported by Alembic
from typing import List, Optional
from src.models.base_model import Base

from src.app.demo.models import Demo
from src.app.team.models import Team, TeamBase
from src.app.hero.models import Hero, HeroBase


# -------------------------------------------
# Nested Models to bypass circle import
# -------------------------------------------


class TeamRead(TeamBase):
    id: str

    heroes: List[Hero] = []


TeamRead.update_forward_refs()


class HeroRead(HeroBase):
    id: str

    team: Optional[Team] = None


HeroRead.update_forward_refs()
