from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client() -> TestClient:
    from backend.api.app import create_app

    app = create_app()
    with TestClient(app) as testclient:
        yield testclient
