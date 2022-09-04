from http import HTTPStatus
from fastapi.exceptions import HTTPException


from app.models.transactions import Transactions
from app.schemas.transactions import TransactionOut


async def get_transactions_controller(db):
    try:
        transactions = db.query(Transactions).all()

        return [TransactionOut.from_orm(transaction) for transaction in transactions]

    except Exception:
        raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, "Internal server error")
