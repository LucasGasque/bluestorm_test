from datetime import datetime
from app.models.patients import Patients


def test_get_patients(client, db_session):
    mock_user = {"username": "jondoe", "password": "secret"}

    client.post("/users", json=mock_user)
    token = client.post("/token", data=mock_user)

    date_of_birth = datetime.now()

    mock_patient = {
        "uuid": "123456789",
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": date_of_birth,
    }
    db_patient = Patients(**mock_patient)
    db_session.add(db_patient)
    db_session.commit()
    db_session.refresh(db_patient)

    mock_patient["date_of_birth"] = date_of_birth.isoformat()

    response = client.get(
        "/patients",
        headers={"Authorization": "Bearer {}".format(token.json()["access_token"])},
    )

    assert response.status_code == 200
    assert response.json() == [mock_patient]

def test_get_patients_unauthorized(client):
    response = client.get("/patients")

    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}