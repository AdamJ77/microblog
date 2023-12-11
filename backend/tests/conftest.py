from testcontainers.mongodb import MongoDbContainer
from pymongo.database import Database
from backend.domain import entities
from pathlib import Path
import pytest


@pytest.fixture(scope="session")
def mongodb_container():
    with MongoDbContainer() as mongo:
        yield mongo


def insert_post(db: Database):
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
def db(request, mongodb_container) -> Database:
    client = mongodb_container.get_connection_client()
    db = getattr(client, request.node.name)
    insert_post(db)
    insert_post(db)
    return db


@pytest.fixture(autouse=True)
def testdir(monkeypatch, tmpdir) -> Path:
    print(tmpdir)
    monkeypatch.chdir(tmpdir)
    return tmpdir


@pytest.fixture
def media():
    return entities.Media(
        entities.Media.Type.IMAGE, "http://microblog.com/posts/13/image1.jpg"
    )


@pytest.fixture
def post_author():
    return entities.User(id="0", name="Author")


@pytest.fixture
def post(post_author, media):
    from datetime import datetime

    post_date = datetime.utcfromtimestamp(0)
    return entities.Post(
        id="0",
        text="Bajojajo",
        author=post_author,
        media=[media],
        date=post_date,
    )
