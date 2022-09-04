from pydantic import BaseModel
from app.configs.password import verify_password
from app.models.users import Users


class User(BaseModel):
    username: str

    class Config:
        orm_mode = True


class UserInDB(User):
    password: str

    class Config:
        orm_mode = True


def get_user(db, username: str):
    user = db.query(Users).filter(Users.username == username).first()

    return UserInDB.from_orm(user) if user else None


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
