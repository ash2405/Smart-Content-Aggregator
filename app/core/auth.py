from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependency import get_db
from app.core.seciruty import decode_access_token
from app.enums.role import Role
from app.repositories.user import user_get_by_id
from app.exceptions.exceptions_log import ForbiddenException

# use to extract token from header
oauth_schema = OAuth2PasswordBearer(
    tokenUrl="/user/token"
)

async def get_current_user(
        token:str=Depends(oauth_schema),
        db:AsyncSession = Depends(get_db)
):
    payload = decode_access_token(token=token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"}
        )

    user_id = payload.get('sub')

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token payload",
            headers={"WWW-Authenticate": "Bearer"}
        )

    user = await user_get_by_id(
        db=db,
        id=int(user_id)
    )

    if user is None or not user.is_active:
        raise HTTPException(
            status_code=401,
            detail="User not found or inactive",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return user

def require_role(*role:Role):
    async def role_checker(
            current_user= Depends(get_current_user)
    ):
        if current_user.role not in role:
            raise ForbiddenException("You don't have permission to access this resource.")

        return current_user
    
    return role_checker