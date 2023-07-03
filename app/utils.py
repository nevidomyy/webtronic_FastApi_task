import hashlib
import jwt
from datetime import datetime, timedelta
from app.config import settings as cfg
from app.db import schemas as sh


def password_hashing(password: str) -> str:
    """
    Password hashing
    :param password: password
    :return: password hash
    """
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),
                               cfg.SALT, 100000).hex()


def generate_jwt_tokens(account_id: int) -> tuple:
    """
    Generate and get tokens
    :param account_id: account ID
    :return: access token and refresh token
    """
    access_token = jwt.encode(sh.TokenPayload(
        account_id=account_id,
        exp=datetime.utcnow() + timedelta(seconds=cfg.JWT_AUTH_EXP_DELTA_SECONDS)
    ).dict(), cfg.SECRET, cfg.JWT_ALGORITHM)

    refresh_token = jwt.encode(sh.TokenPayload(
        refresh_sec=hashlib.sha256(access_token.encode('utf-8')).hexdigest(),
        account_id=account_id,
        exp=datetime.utcnow() + timedelta(seconds=cfg.JWT_REFRESH_EXP_DELTA_SECONDS)
    ).dict(), cfg.SECRET, cfg.JWT_ALGORITHM)

    return access_token, refresh_token
