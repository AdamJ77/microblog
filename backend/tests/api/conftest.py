from fastapi.testclient import TestClient
from backend.api.app import Database
import pytest


@pytest.fixture
def client(request, monkeypatch, mongodb_container) -> TestClient:
    from backend.api.app import create_app

    monkeypatch.setenv(
        "DB_CONNECTION_URL", mongodb_container.get_connection_url()
    )
    monkeypatch.setattr(Database, "instance_name", request.node.name)

    app = create_app()
    with TestClient(app) as testclient:
        yield testclient


@pytest.fixture
def db(request, mongodb_container) -> Database:
    client = mongodb_container.get_connection_client()
    db = getattr(client, request.node.name)
    return db
