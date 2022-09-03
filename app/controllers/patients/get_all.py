from http import HTTPStatus
from fastapi.exceptions import HTTPException


from app.models.patients import Patients
from app.schemas.patients import PatientOut


async def get_patients_controller(db):
    try:
        patients = db.query(Patients).all()
        return [PatientOut.from_orm(patient) for patient in patients]

    except Exception:
        raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, "Internal server error")
