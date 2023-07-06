from datetime import datetime

from fastapi import HTTPException
from sqlalchemy import (
    Column, String, Integer, ForeignKey,
    DateTime, Text, Boolean, UniqueConstraint, Null
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True, unique=True)
    date_joined = Column(DateTime, default=datetime.utcnow())
    last_login = Column(DateTime, default=datetime.utcnow())
    is_active = Column(Boolean, default=True)
    password = Column(String(255), nullable=True)


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text, nullable=False, min_length=10)
    date_edited = Column(DateTime, default=datetime.utcnow())
    user_id = Column(ForeignKey('user.id'), nullable=False)


class Like(Base):
    __tablename__ = 'like'

    post_id = Column(ForeignKey('post.id', ondelete='CASCADE'),
                     nullable=False, primary_key=True)
    user_id = Column(ForeignKey('user.id', ondelete='CASCADE'),
                     nullable=False, primary_key=True)
    like = Column(Boolean, default=Null)

    __table_args__ = (
        UniqueConstraint('post_id', 'user_id', name='uq_post_user_like'),
    )
