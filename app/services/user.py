from sqlalchemy.ext.asyncio import AsyncSession

from app.core.seciruty import create_access_token, verify_password
from app.repositories.user import create_user, user_get_by_email , user_get_by_id
from app.schemas.user import UserCreate, UserLogin
from app.exceptions.exceptions_log import BadRequestException, ForbiddenException , NotFoundException

async def create_user_service(
        data:UserCreate,
        db:AsyncSession
):
    user_email = await user_get_by_email(
        email=data.email,
        db=db
    )

    if user_email is not None:
        raise BadRequestException("Email already Exist.")

    try:
        user = await create_user(
            data=data,
            db=db
        )

        await db.commit()
        await db.refresh(user)

        return user
    except Exception:
        await db.rollback()
        raise

async def get_user_by_id(
        id:int,
        db:AsyncSession,
        current
):
    if current.id != id:
          raise ForbiddenException("You cannot access another user's profile.")
    user_detail = await user_get_by_id(
        id=id,
        db=db
    )
    if user_detail is None:
        raise NotFoundException(f'User with id: {id} is not found!')

    return user_detail

async def user_login_service(
        data: UserLogin,
        db:AsyncSession
):
    
    user = await user_get_by_email(
            email=data.email,
            db=db
        )
    
    if user is None:
        raise BadRequestException("Invalid credentials.")

    hashed_password = verify_password(
        password=data.password,
        hash_password=user.password
    )

    if hashed_password == False:
        raise BadRequestException("Invalid credentials.")

    access_token = create_access_token(
        data={
            "sub":str(user.id)
        }
    )


    return {
        "access_token": access_token,
        "token_type": "bearer"
    }