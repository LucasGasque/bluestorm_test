from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db

from app.controllers.patients.get_all import get_patients_controller


patients = APIRouter(prefix="/patients", tags=["patients"])


@patients.get("")
async def get_patients(db: Session = Depends(get_db)):
    return await get_patients_controller(db)
