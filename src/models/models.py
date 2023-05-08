# Import all the models, so that Base has them before being
# imported by Alembic
from typing import List, Optional
from src.models.base_model import Base

from src.app.demo.models import Demo
from src.app.team.models import Team, TeamBase, TeamRead
from src.app.hero.models import Hero, HeroBase, HeroRead


# -------------------------------------------
# Nested Models to bypass circle import
# -------------------------------------------


class TeamWithHeroes(TeamBase):
    id: str

    heroes: List[HeroRead] = []


TeamWithHeroes.update_forward_refs()


class HeroDetail(HeroBase):
    id: str

    team: Optional[TeamRead] = None


HeroDetail.update_forward_refs()
