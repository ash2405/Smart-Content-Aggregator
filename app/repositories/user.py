from sqlalchemy import select
from sqlalchemy.ext.asyncio import  AsyncSession

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.seciruty import hash_password

async def create_user(
        data:UserCreate,
        db:AsyncSession
):
    new_user = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password)
    )

    db.add(new_user)
    await db.flush()

    return new_user

async def user_get_by_email(
        email:str,
        db:AsyncSession
):
    user = await db.execute(
        select(User).where(User.email == email)
    )

    return user.scalar_one_or_none()

async def user_get_by_id(
        id:int,
        db:AsyncSession
):
    user = await db.execute(
        select(User).where(User.id == id)
    )

    return user.scalar_one_or_none()