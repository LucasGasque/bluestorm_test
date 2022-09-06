from http import HTTPStatus
from fastapi.exceptions import HTTPException


from app.models.patients import Patients
from app.schemas.patients import PatientOut


async def get_patients_controller(db, first_name, last_name):
    try:
        patients = db.query(Patients)

        if first_name:
            patients = patients.filter(Patients.first_name.like(f"%{first_name}%"))

        if last_name:
            patients = patients.filter(Patients.last_name.like(f"%{last_name}%"))

        patients = patients.all()

        return [PatientOut.from_orm(patient) for patient in patients]

    except Exception:
        raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, "Internal server error")
