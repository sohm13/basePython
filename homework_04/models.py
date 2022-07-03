"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Text
)   

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship, declared_attr


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"


class Base:

    @declared_attr
    def __tablename__(self):
        return f"{self.__name__}"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)

engine = create_async_engine(PG_CONN_URI, echo=False)
Base = declarative_base(bind=engine, cls=Base)
Session = sessionmaker(bind=engine, class_=AsyncSession)
# Session = scoped_session(sessionmaker(bind=engine, class_=AsyncSession))


class User(Base):

    name = Column(String(60), nullable=False)
    username = Column(String(60), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.name}"

class Post(Base):

    user_id = Column(Integer, ForeignKey("User.id"), nullable=False, unique=False)
    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=True, default="")

    user = relationship("User", back_populates="posts")
    
    def __str__(self):
        return f"{self.user_id}"