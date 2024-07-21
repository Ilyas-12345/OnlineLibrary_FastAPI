from sqlalchemy import String, Integer, Column, ForeignKey, MetaData
from sqlalchemy.orm import DeclarativeBase, relationship
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase


class Base(DeclarativeBase):
    metadata = MetaData()


class User(Base):
    __tablename__ = ('user')

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(20), nullable=False)
    last_name: str = Column(String(20), nullable=False)
    email: str = Column(String, nullable=False)
    hash_password: str = Column(String, nullable=False)