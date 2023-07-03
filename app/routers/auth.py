from datetime import datetime

from fastapi import APIRouter, HTTPException
from sqlalchemy import and_
from starlette.status import HTTP_403_FORBIDDEN

from app.db.models import User
from app.db.schemas import AuthResponseModel
from app.services.db.sqlalchemy import service_session
from app.db import schemas
from app.utils import generate_jwt_tokens, password_hashing

router = APIRouter()


@router.post('/registration')
async def registration(data: schemas.RegisterUser) -> AuthResponseModel:
    """
    Register new user in database
    """
    with service_session() as session:
        if user_obj := session.query(User).filter_by(email=data.email).first():
            raise HTTPException(status_code=409, detail='Already Exists')

        user_obj = User(**data.dict())
        session.add(user_obj)
        session.commit()
        session.refresh(user_obj)

    access_token, refresh_token = generate_jwt_tokens(user_obj.id)
    return AuthResponseModel(access_token=access_token,
                             refresh_token=refresh_token)


@router.post('/login')
async def login(data: schemas.LoginUser):
    """
    <h3>Available exceptions:</h3>
    <ul>
        <li>{"success": false, "code": 403, "data": "Not authenticated"}</li>
        <li>{"success": false, "code": 403, "data": "Invalid token"}</li>
        <li>{"success": false, "code": 403, "data": "Expired signature"}</li>
        <li>{"success": false, "code": 403, "data": "Wrong username or password!"}</li>
    </ul>
    """
    with service_session() as session:
        user_obj = session.query(User).filter(and_(
            User.email == data.email)).first()
        if not user_obj:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN)

        if user_obj.password == password_hashing(data.password):
            access_token, refresh_token = generate_jwt_tokens(user_obj.id)
            user_obj.last_login = datetime.utcnow()
            session.commit()
            return AuthResponseModel(
                            access_token=access_token,
                            refresh_token=refresh_token
                        )
        else:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN)
