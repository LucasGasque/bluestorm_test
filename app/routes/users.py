from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db

users = APIRouter(prefix="/users", tags=["users"])


@users.get("")
async def get_users():
    return
