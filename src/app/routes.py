from fastapi import FastAPI

from src.app.demo.router import router as demo_router
from src.app.team.router import router as team_router
from src.app.hero.router import router as hero_router


def init_routes(app: FastAPI):
    app.include_router(demo_router, prefix="", tags=["Demo"])
    app.include_router(team_router, prefix="", tags=["Teams"])
    app.include_router(hero_router, prefix="", tags=["Heroes"])
