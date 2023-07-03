from fastapi import Depends, HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from sqlalchemy import and_

from .token_payload import token_payload, TokenPayload
from app.services.db.sqlalchemy import service_session
from app.db.models import User


def _get_user(_token_payload: TokenPayload = token_payload()) -> User:
    with service_session() as session:
        user = session.query(User).filter(and_(
            User.id == _token_payload.account_id)).first()
        if not user:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN)
        return user


def get_user():
    return Depends(_get_user)

