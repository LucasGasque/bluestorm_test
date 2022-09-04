from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.configs.database import Base


class Pharmacies(Base):
    __tablename__ = "pharmacies"

    uuid = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String, index=True)
