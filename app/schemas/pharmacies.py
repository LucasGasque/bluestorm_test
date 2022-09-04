from pydantic import BaseModel


class PharmacieOut(BaseModel):
    uuid: str
    name: str
    city: str

    class Config:
        orm_mode = True
