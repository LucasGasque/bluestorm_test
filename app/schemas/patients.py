from datetime import datetime
from pydantic import BaseModel


class PatientOut(BaseModel):
    uuid: str
    first_name: str
    last_name: str
    date_of_birth: datetime

    class Config:
        orm_mode = True
