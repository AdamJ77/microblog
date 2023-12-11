from fastapi.testclient import TestClient
from backend.api.database.db import Database
import pytest


@pytest.fixture
def client(monkeypatch, mongodb_container, db) -> TestClient:
    from backend.api.app import create_app

    monkeypatch.setenv(
        "DB_CONNECTION_URL", mongodb_container.get_connection_url()
    )

    async def mock_database(_):
        return db

    monkeypatch.setattr(Database, "database", property(mock_database))

    app = create_app()
    with TestClient(app) as testclient:
        yield testclient
