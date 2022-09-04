from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.configs.database import get_db
from app.configs.token import Token
from app.controllers.users.create import create_user_controller
from app.controllers.users.login import login_user_controller
from app.schemas.users import UserIn

users = APIRouter(tags=["users"])


@users.post("/users")
async def create_user(user: UserIn, db: Session = Depends(get_db)):
    return await create_user_controller(user, db)


@users.post("/token", response_model=Token)
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    return await login_user_controller(form_data, db)
