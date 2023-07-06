from datetime import datetime
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, validator
from app.config import settings as cfg
from app.db import models
from app.services.db.sqlalchemy import service_session
from app.utils import password_hashing


class RegisterUser(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    @validator('password')
    def password_validator(cls, value):
        if value:
            return password_hashing(value)
        return value

    @validator('first_name', 'last_name')
    def validate_name(cls, value):
        if len(value) < 1:
            raise HTTPException(
                status_code=403,
                detail="The 'text' field must have a "
                       "minimum length of 1 characters.")

        if '\u0000' in value:
            raise ValueError("Text cannot contain null character (\\u0000)")
        return value


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class AuthResponseModel(BaseModel):
    access_token: str
    refresh_token: str
    access_token_expire: int = cfg.JWT_AUTH_EXP_DELTA_SECONDS
    refresh_token_expire: int = cfg.JWT_REFRESH_EXP_DELTA_SECONDS


class TokenPayload(BaseModel):
    refresh_sec: Optional[str]
    account_id: int
    exp: datetime


class PostList(BaseModel):
    id: int
    text: str
    date_edited: datetime
    user_id: int


class CreatePostModel(BaseModel):
    text: str

    @validator('text')
    def text_validator(cls, value):
        if '\u0000' in value:
            raise ValueError("Text cannot contain null character (\\u0000)")
        return value


class PostDetail(BaseModel):
    id: int
    text: str
    date_edited: datetime
    user_id: int


class PostUpdate(BaseModel):
    text: str
    date_edited: datetime


class PostId(BaseModel):
    post_id: int

    @validator('post_id')
    def validate_post(cls, value):
        with service_session() as session:
            if not session.query(models.Post).filter(
                    models.Post.id == value).first():
                raise HTTPException(
                    status_code=404,
                    detail=f'Post with id {value} does not exist'
                )
        return value
