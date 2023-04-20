# Import all the models, so that Base has them before being
# imported by Alembic
from src.base_model import Base

from src.demo.models import Demo
from src.team.models import Team
from src.hero.models import Hero
