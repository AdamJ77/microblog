from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client(monkeypatch, mongodb_container) -> TestClient:
    from backend.api.app import create_app

    monkeypatch.setenv(
        'DB_CONNECTION_URL', mongodb_container.get_connection_url())
    app = create_app()
    with TestClient(app) as testclient:
        yield testclient
