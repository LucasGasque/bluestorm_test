from datetime import datetime
from app.models.transactions import Transactions


def test_get_pharmacies(client, db_session):
    mock_user = {"username": "jondoe", "password": "secret"}

    client.post("/users", json=mock_user)
    token = client.post("/token", data=mock_user)

    timestamp = datetime.now()

    mock_transaction = {
        "uuid": "123456789",
        "patient_uuid": "123456789",
        "pharmacy_uuid": "123456789",
        "amount": 100,
        "timestamp": timestamp,
    }
    db_transaction = Transactions(**mock_transaction)
    db_session.add(db_transaction)
    db_session.commit()
    db_session.refresh(db_transaction)

    response = client.get(
        "/transactions",
        headers={"Authorization": "Bearer {}".format(token.json()["access_token"])},
    )

    mock_transaction["timestamp"] = timestamp.isoformat()

    assert response.status_code == 200
    assert response.json() == [mock_transaction]


def test_get_pharmacies_unauthorized(client):
    response = client.get("/transactions")

    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}
