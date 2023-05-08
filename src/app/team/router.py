from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.database.database import get_db

from src.app.team.models import Team, TeamRead, TeamCreate, TeamUpdate
from src.models.models import TeamWithHeroes

router = APIRouter()

team_router = SQLAlchemyCRUDRouter(
    schema=TeamRead,
    create_schema=TeamCreate,
    update_schema=TeamUpdate,
    detail_schema=TeamWithHeroes,
    db_model=Team,
    db=get_db,
)

router.include_router(team_router)
