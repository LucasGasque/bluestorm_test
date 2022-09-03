from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db

pharmacies = APIRouter(prefix="/pharmacies", tags=["pharmacies"])


@pharmacies.get("")
async def get_pharmacies():
    return
