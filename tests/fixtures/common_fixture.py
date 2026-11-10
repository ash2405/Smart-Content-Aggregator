from fastapi.testclient import TestClient
import pytest

from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as tst_client:
        yield tst_client