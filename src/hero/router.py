from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.database import get_db

from src.hero.models import Hero, HeroCreate, HeroUpdate
from src.models import HeroRead

router = APIRouter()

hero_router = SQLAlchemyCRUDRouter(
    schema=HeroRead,
    create_schema=HeroCreate,
    update_schema=HeroUpdate,
    db_model=Hero,
    db=get_db,
)

router.include_router(hero_router)
