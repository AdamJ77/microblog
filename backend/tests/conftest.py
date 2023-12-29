from testcontainers.mongodb import MongoDbContainer
from backend.domain import entities
from pathlib import Path
import pytest


@pytest.fixture(scope="session")
def mongodb_container():
    with MongoDbContainer() as mongo:
        yield mongo


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
    return entities.User(id="213", name="Greg")


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
