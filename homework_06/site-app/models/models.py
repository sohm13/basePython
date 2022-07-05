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
from models.database import  db



class Base(db.Model):

    @declared_attr
    def __tablename__(self):
        return f"{self.__name__}"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)

# engine = create_async_engine(PG_CONN_URI, echo=False)
# Base = declarative_base(bind=engine, cls=Base)
# Session = sessionmaker(bind=engine, class_=AsyncSession)
# # Session = scoped_session(sessionmaker(bind=engine, class_=AsyncSession))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    username = Column(String(60), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.name}"



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, unique=False)
    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=True, default="")

    user = relationship("User", back_populates="posts")
    
    def __str__(self):
        return f"{self.user_id}"