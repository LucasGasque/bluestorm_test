from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db

transactions = APIRouter(prefix="/transactions", tags=["transactions"])


@transactions.get("")
async def get_transactions():
    return
