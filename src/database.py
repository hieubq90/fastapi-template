from functools import lru_cache
from sqlalchemy import (
    # MetaData,
    create_engine,
)
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, MetaData
from src.config import settings
from src.constants import DB_NAMING_CONVENTION


DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
metadata = SQLModel.metdata
# metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)


# Re-use database engine
@lru_cache(maxsize=None)
def get_engine():
    return create_engine(DATABASE_URL, pool_pre_ping=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())


# Dependency: One session per request
def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()
