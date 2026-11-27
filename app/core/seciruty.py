from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(
    schemes=['bcrypt'],
    deprecated = "auto"
)


def hash_password(passowrd:str)-> str:
    return pwd_context.hash(passowrd)


def verify_password(
        password: str,
        hash_password:str
)->bool:

    return pwd_context.verify(password,hash_password)


def create_access_token(data : dict) -> str:

    to_encoded = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_expiry_minutes
    )

    to_encoded.update({
        'exp':expire
    })

    encoded_jwt = jwt.encode(
        to_encoded,
        settings.secret_key,
        algorithm=settings.algorithm
    )

    return encoded_jwt

def decode_access_token(token:str):
    try:
        payload = jwt.decode(
                        token,
                        settings.secret_key,
                        algorithms=[settings.algorithm]
                    )
        return payload
    
    except jwt.InvalidTokenError:
        None
    