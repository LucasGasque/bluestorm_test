from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.configs.database import Base
from app.models.patients import Patients


class Transactions(Base):
    __tablename__ = "transactions"

    uuid = Column(String, primary_key=True, index=True)
    patient_uuid = Column(String, ForeignKey("patients.uuid"))
    pharmacy_uuid = Column(String, ForeignKey("pharmacies.uuid"))
    amount = Column(Integer)
    timestamp = Column(DateTime)
