from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.database import get_db

from src.team.models import Team, TeamCreate, TeamUpdate
from src.models import TeamRead

router = APIRouter()

team_router = SQLAlchemyCRUDRouter(
    schema=TeamRead,
    create_schema=TeamCreate,
    update_schema=TeamUpdate,
    db_model=Team,
    db=get_db,
)

router.include_router(team_router)
