from pathlib import Path

from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client() -> TestClient:
    from backend.api.app import create_app

    app = create_app()
    return TestClient(app)


@pytest.fixture(autouse=True)
def testdir(monkeypatch, tmpdir) -> Path:
    print(tmpdir)
    monkeypatch.chdir(tmpdir)
    return tmpdir
