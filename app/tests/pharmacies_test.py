from app.models.pharmacies import Pharmacies


def test_get_pharmacies(client, db_session):
    mock_user = {"username": "jondoe", "password": "secret"}

    client.post("/users", json=mock_user)
    token = client.post("/token", data=mock_user)

    mock_pharmacy = {
        "uuid": "123456789",
        "name": "Drogasil",
        "city": "São Paulo",
    }
    db_pharmacy = Pharmacies(**mock_pharmacy)
    db_session.add(db_pharmacy)
    db_session.commit()
    db_session.refresh(db_pharmacy)

    response = client.get(
        "/pharmacies",
        headers={"Authorization": "Bearer {}".format(token.json()["access_token"])},
    )

    assert response.status_code == 200
    assert response.json() == [mock_pharmacy]


def test_get_pharmacies_unauthorized(client):
    response = client.get("/pharmacies")

    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}
