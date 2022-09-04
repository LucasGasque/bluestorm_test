from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db
from app.configs.token import get_current_user
from app.controllers.pharmacies.get_all import get_pharmacies_controller

pharmacies = APIRouter(prefix="/pharmacies", tags=["pharmacies"])


@pharmacies.get("")
async def get_pharmacies(
    db: Session = Depends(get_db), _: str = Depends(get_current_user)
):
    return await get_pharmacies_controller(db)
