import jwt
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN


from app.db.schemas import TokenPayload
from app.config import settings as cfg


token_scheme = APIKeyHeader(name='Authorization')


async def _token_payload(token: str = Depends(token_scheme)) -> TokenPayload:
    """
    Decoded access token
    :param token: access token
    :return: account ID
    """
    try:
        payload = jwt.decode(token, cfg.SECRET, cfg.JWT_ALGORITHM)
    except jwt.DecodeError:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail='Invalid token')
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail='Expired signature')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)
    else:
        return TokenPayload(**payload)


def token_payload():
    return Depends(_token_payload)


