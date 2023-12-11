from fastapi.testclient import TestClient
from backend.api.app import Database
import pytest


def insert_example_post(db):
    post = {
        "type": "posts",
        "attributes": {
            "author": {
                "id": "213",
                "attributes": {
                    "name": "Greg",
                    "avatar": {
                        "src": "http://microblog.com/users/avatars/Greg.png"
                    },
                },
            },
            "text": "Bajojajo",
            "created": "2023-04-20T18:34:59.213Z",
            "media": [
                {
                    "type": "image",
                    "src": "http://microblog.com/posts/13/image1.jpg",
                }
            ],
        },
    }
    db["posts"].insert_one(post)


@pytest.fixture
def client(request, monkeypatch, mongodb_container) -> TestClient:
    from backend.api.app import create_app

    monkeypatch.setenv(
        "DB_CONNECTION_URL", mongodb_container.get_connection_url()
    )

    monkeypatch.setattr(
        Database, "get_instance_name", lambda _: request.node.name
    )

    client = mongodb_container.get_connection_client()
    db = getattr(client, request.node.name)
    insert_example_post(db)
    insert_example_post(db)

    app = create_app()
    with TestClient(app) as testclient:
        yield testclient
