import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.auth.auther import auth_backend
from src.auth.db import User
from src.auth.schemas import UserRead, UserCreate
from src.auth.user_manager import get_user_manager

app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",port=8080, log_level="info")