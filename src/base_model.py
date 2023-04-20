import uuid
from typing import Optional

# from pydantic import Extra
# from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import (
    Column,
    String,
    BigInteger,
    Boolean,
    event,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, SQLModel
from src.helpers import now_timestamp

# from src.database import metadata


def default_uuid():
    return str(uuid.uuid4())


# @as_declarative()
# class Base(SQLModel):
#     __tablename__ = ""
#     metadata = metadata
#     id = Column(uuid.UUID, primary_key=True, default=default_uuid)
#     created_at = Column(BigInteger, index=True, default=now_timestamp)
#     created_by = Column(uuid.UUID, nullable=True)
#     created_by_name = Column(String())

#     updated_at = Column(BigInteger, index=True, default=now_timestamp)
#     updated_by = Column(uuid.UUID, nullable=True)
#     updated_by_name = Column(String())

#     deleted = Column(Boolean, index=True, default=False)
#     deleted_at = Column(BigInteger, index=True)
#     deleted_by = Column(uuid.UUID, nullable=True)
#     deleted_by_name = Column(String())
#     __name__: str

#     # Generate __tablename__ automatically
#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()

#     # @declared_attr
#     # def __config__(cls) -> str:
#     #     return {"table": True, "extra": Extra.allow}

#     def to_dict(self):
#         return self.columns_to_dict()

#     def columns_to_dict(self):
#         dict_ = {}
#         for key in self.__mapper__.c.keys():
#             dict_[key] = getattr(self, key)
#             if type(dict_[key]) == uuid.UUID:
#                 dict_[key] = str(dict_[key])

#         return dict_


class Base(SQLModel):
    __tablename__ = ""

    id: str = Field(
        primary_key=True,
        default=None,
        sa_column=Column(String(), primary_key=True),
    )
    created_at: int = Field(
        index=True, default=now_timestamp(), sa_column=Column(BigInteger())
    )
    created_by: Optional[str] = Field(default=None, sa_column=Column(String()))
    created_by_name: Optional[str] = Field(default=None, sa_column=Column(String()))

    updated_at: int = Field(
        index=True, default=now_timestamp(), sa_column=Column(BigInteger())
    )
    updated_by: Optional[str] = Field(default=None, sa_column=Column(String()))
    updated_by_name: Optional[str] = Field(default=None, sa_column=Column(String()))

    deleted: bool = Field(index=True, default=False, sa_column=Column(Boolean))
    deleted_at: Optional[int] = Field(
        index=True, default=None, sa_column=Column(BigInteger)
    )
    deleted_by: Optional[str] = Field(default=None, sa_column=Column(String()))
    deleted_by_name: Optional[str] = Field(default=None, sa_column=Column(String()))


def on_before_create_event(mapper, connection, instance):
    print(f"instance: {instance} | mapper: {mapper}")
    timestamp = now_timestamp()
    instance.id = default_uuid()
    instance.created_at = timestamp
    instance.updated_at = timestamp
    print(f"instance: {instance} | mapper: {mapper}")


def on_before_update_event(mapper, connection, instance):
    timestamp = now_timestamp()
    if not instance.deleted:
        timestamp = now_timestamp()
        instance.updated_at = timestamp
        
    if instance.deleted is True:
        instance.deleted_at = timestamp


event.listen(Base, "before_insert", on_before_create_event, propagate=True)
event.listen(Base, "before_update", on_before_update_event, propagate=True)
