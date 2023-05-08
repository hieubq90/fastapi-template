from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.database.database import get_db

from src.app.hero.models import Hero, HeroRead, HeroCreate, HeroUpdate
from src.models.models import HeroDetail

router = APIRouter()

hero_router = SQLAlchemyCRUDRouter(
    schema=HeroRead,
    create_schema=HeroCreate,
    update_schema=HeroUpdate,
    detail_schema=HeroDetail,
    db_model=Hero,
    db=get_db,
)

router.include_router(hero_router)
