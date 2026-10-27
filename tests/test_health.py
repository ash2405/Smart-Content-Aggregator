
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_sources():
    response = client.get("/sources/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_source_not_found():
    response = client.get("/sources/999999")

    assert response.status_code == 404


def test_update_source_not_found():
    response = client.put(
        "/sources/999999",
        json={
            "name": "Test Source",
            "url": "https://example.com/test-source",
        },
    )

    assert response.status_code == 404
