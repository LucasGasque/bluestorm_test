from datetime import datetime
from pydantic import BaseModel

from app.schemas.patients import PatientOut
from app.schemas.pharmacies import PharmacieOut


class TransactionOut(BaseModel):
    uuid: str
    patient_uuid: str
    pharmacy_uuid: str
    amount: int
    timestamp: datetime

    class Config:
        orm_mode = True
