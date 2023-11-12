from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client() -> TestClient:
    from api.app import create_app

    app = create_app()
    return TestClient(app)
