from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db
from app.configs.token import get_current_user
from app.controllers.transactions.get_all import get_transactions_controller

transactions = APIRouter(prefix="/transactions", tags=["transactions"])


@transactions.get("")
async def get_transactions(
    db: Session = Depends(get_db), _: str = Depends(get_current_user)
):
    return await get_transactions_controller(db)
