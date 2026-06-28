from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_user() -> None:
    response = client.get("/user/1")

    assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "data": {
            "id": 1,
            "name": "Taro",
            "display_name": "User: Taro",
        },
    }


def test_get_user_not_found() -> None:
    response = client.get("/user/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
