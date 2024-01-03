from testcontainers.mongodb import MongoDbContainer
from backend.domain import entities
from pathlib import Path
import pytest
import hashlib
import asyncio


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


@pytest.fixture(autouse=True)
def setup_event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


async def async_get_user(client):
    db = client.app.database

    # Wstawianie nowego użytkownika do bazy danych
    inserted_result = await db.users.insert_one({
        "login": "fake_login",
        "password": hashlib.sha256("fake_password".encode()).hexdigest(),
        "avatar": "http://microblog/avatar.jpg",
        "username": "user1"
    })

    # Pobieranie _id (ObjectId) z wyniku wstawiania i konwersja na string
    user_id = str(inserted_result.inserted_id)

    return user_id


@pytest.fixture
def get_user(client):
    return asyncio.run(async_get_user(client))
