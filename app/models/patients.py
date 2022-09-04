from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.configs.database import Base


class Patients(Base):
    __tablename__ = "patients"

    uuid = Column(String, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    date_of_birth = Column(DateTime, index=True)
