from pydantic import BaseModel


class UserOut(BaseModel):
    uuid: str
    username: str
    password: str

    class Config:
        orm_mode = True


class UserIn(BaseModel):
    username: str
    password: str
