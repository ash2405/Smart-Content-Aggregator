from pydantic import BaseModel

from app.enums.role import Role


class UserLogin(BaseModel):
    email: str
    password: str

class UserCreate(UserLogin):
    name: str
    is_active:bool = True
    role: Role = Role.USER

class UserResponse(UserCreate):
    id: int
    model_config = {
        "from_attributes": True
    }
