from enum import unique
from uuid import uuid4
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.configs.database import Base


class Users(Base):
    __tablename__ = "users"

    uuid = Column(
        String,
        primary_key=True,
        index=True,
        default=uuid4().hex,
    )
    username = Column(String, unique=True, index=True)
    password = Column(String, index=True)
