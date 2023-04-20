import uuid

# from pydantic import Extra
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import (
    Column,
    String,
    BigInteger,
    Boolean,
    event,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import SQLModel
from src.helpers import now_timestamp

from src.database import metadata


def default_uuid():
    return str(uuid.uuid4())


@as_declarative()
class Base(SQLModel):
    __tablename__ = ""
    metadata = metadata
    id = Column(UUID(as_uuid=True), primary_key=True, default=default_uuid)
    created_at = Column(BigInteger, index=True, default=now_timestamp)
    created_by = Column(UUID(as_uuid=True), nullable=True)
    created_by_name = Column(String())

    updated_at = Column(BigInteger, index=True, default=now_timestamp)
    updated_by = Column(UUID(as_uuid=True), nullable=True)
    updated_by_name = Column(String())

    deleted = Column(Boolean, index=True, default=False)
    deleted_at = Column(BigInteger, index=True)
    deleted_by = Column(UUID(as_uuid=True), nullable=True)
    deleted_by_name = Column(String())
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    # @declared_attr
    # def __config__(cls) -> str:
    #     return {"table": True, "extra": Extra.allow}

    def to_dict(self):
        return self.columns_to_dict()

    def columns_to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
            if type(dict_[key]) == uuid.UUID:
                dict_[key] = str(dict_[key])

        return dict_


def on_before_create_event(mapper, connection, instance):
    print(f"instance: {instance} | mapper: {mapper}")
    timestamp = now_timestamp()
    instance.created_at = timestamp

    # instance.updated_at = timestamp


def on_before_update_event(mapper, connection, instance):
    timestamp = now_timestamp()
    instance.created_at = (
        instance.created_at if instance.created_at is not None else timestamp
    )
    # instance.updated_at = timestamp
    if instance.deleted is True:
        instance.deleted_at = timestamp


event.listen(Base, "before_insert", on_before_create_event, propagate=True)
event.listen(Base, "before_update", on_before_update_event, propagate=True)
