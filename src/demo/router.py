from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.database import get_db

from src.demo.models import Demo, DemoCreate

router = APIRouter()

demo_router = SQLAlchemyCRUDRouter(
    schema=Demo, create_schema=DemoCreate, update_schema=DemoCreate, db_model=Demo, db=get_db
)

router.include_router(demo_router)
