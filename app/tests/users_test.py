from app.configs.password import verify_password


def test_create_user(client):
    mock_user = {"username": "jondoe", "password": "secret"}

    response = client.post("/users", json=mock_user)

    assert response.status_code == 200
    assert response.json()["username"] == mock_user["username"]
    assert verify_password(mock_user["password"], response.json()["password"])


def test_create_existing_user(client):
    mock_user = {"username": "jondoe", "password": "secret"}

    client.post("/users", json=mock_user)
    response = client.post("/users", json=mock_user)

    assert response.status_code == 400
    assert response.json() == {"detail": "Username already exists"}


def test_login_user(client):
    session = client
    headers = {"content-type": "multipart/form-data"}

    mock_user = {"username": "jondoe", "password": "secret"}

    session.post("/users", json=mock_user)
    response = session.post("/token", json=mock_user, headers=headers)

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()
