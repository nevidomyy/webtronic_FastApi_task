from datetime import datetime

from sqlalchemy import (Column, String, Integer, ForeignKey,
                        DateTime, Text, Boolean)
from sqlalchemy.ext.declarative import declarative_base

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
    language_id = Column(ForeignKey('language.language_code'), nullable=False)


class Language(Base):
    __tablename__ = 'language'

    language_code = Column(String(2), primary_key=True)


class Post(Base):
    __tablename__ = 'post'
