from http import HTTPStatus
from fastapi.exceptions import HTTPException


from app.models.pharmacies import Pharmacies
from app.schemas.pharmacies import PharmacieOut


async def get_pharmacies_controller(db):
    try:
        pharmacies = db.query(Pharmacies).all()
        return [PharmacieOut.from_orm(pharmacy) for pharmacy in pharmacies]

    except Exception:
        raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, "Internal server error")
