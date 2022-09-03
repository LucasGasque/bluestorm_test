from fastapi import APIRouter
from .patients import patients
from .pharmacies import pharmacies
from .transactions import transactions
from .users import users

router = APIRouter()

router.include_router(patients)
router.include_router(pharmacies)
router.include_router(transactions)
router.include_router(users)