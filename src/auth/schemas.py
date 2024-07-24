from fastapi_users import schemas
from fastapi_users.schemas import PYDANTIC_V2
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    username: str
    password: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserUpdate(schemas.BaseUserUpdate):
    password: str = None
    username: str = None
    email: EmailStr = None
    is_active: bool = None
    is_superuser: bool = None
    is_verified: bool = None