from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.core.auth import get_current_user, require_role
from app.core.dependency import get_db
from app.enums.role import Role
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services.user import create_user_service, get_user_by_id, user_login_service


router = APIRouter(
    prefix='/user',
    tags=["User"]
)

@router.get('/{id}',response_model=UserResponse)
async def get_user_detail(
    id:int,
    db:AsyncSession = Depends(get_db),
    current = Depends(get_current_user)
):
    return await get_user_by_id(
        id=id,
        db=db,
        current=current
    )

@router.post('/',response_model=UserResponse)
async def create_user(
    data:UserCreate,
    db:AsyncSession = Depends(get_db)
):

    return await create_user_service(
        db=db,
        data=data
    )

@router.post('/login')
async def login(
    data: UserLogin,
    db:AsyncSession = Depends(get_db)
):
    return await user_login_service(
        data=data,
        db=db
    )

@router.post('/token')
async def token(
    data: OAuth2PasswordRequestForm = Depends(),
    
    db:AsyncSession = Depends(get_db)
):
    user_data = UserLogin(
        email=data.username,
        password=data.password
    )
    return await user_login_service(
        data=user_data,
        db=db
    )

@router.get('/admin/dashboard')
async def get_dashboard(
    current_user= Depends(require_role(Role.ADMIN))
):
    return {
        "message": "Welcome to Admin Dashboard",
        "admin_id": current_user.id,
        "role": current_user.role
    }
