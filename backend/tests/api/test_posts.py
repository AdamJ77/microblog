from backend.api.routers import posts
from datetime import datetime
import pytest
import random
import string
import hashlib

ADD_POST_REQUEST = {
    "data": {
        "type": "posts",
        "attributes": {
            "body": "Bajojajo",
            "media": [
                {
                    "type": "image",
                    "src": "http://microblog.com/posts/13/image1.jpg",
                }
            ],
        },
    }
}


def signup_user(client):
    body = {
        "username": "Greg",
        "login": ''.join(random.choice(
            string.ascii_letters + string.digits) for _ in range(10)),
        "password": hashlib.sha256("fake_password".encode()).hexdigest(),
        "avatar": "http://microblog.com/avatars/Greg.png"
    }
    response = client.post("/api/auth/signup", json=body).json()
    return response


@pytest.fixture
def insert_example_posts(request, db, post):
    from backend.api.database.adapters import post_to_doc
    from pytest import Mark

    marker: Mark = request.node.get_closest_marker("count")
    post_doc = post_to_doc(post)
    del post_doc["_id"]

    for collection in marker.kwargs:
        count = marker.kwargs[collection]
        for _ in range(count):
            db[collection].insert_one(post_doc.copy())


def check_get_posts_response(response, check_date=True):
    assert response["links"]["self"]
    assert response["links"]["next"]

    for post in response["data"]:
        assert post["type"] == "posts"

        avatar_src = "http://microblog.com/avatars/Greg.png"
        author = post["attributes"]["author"]
        assert author["attributes"]["name"] == "Greg"
        assert author["attributes"]["avatar"]["src"] == avatar_src

        assert post["attributes"]["body"] == "Bajojajo"
        assert (
            post["attributes"]["created"] == "1970-01-01T00:00:00.000Z"
            or not check_date
        )

        media = post["attributes"]["media"]
        assert len(media) == 1
        for m in media:
            assert m["type"] == "image"
            assert m["src"] == "http://microblog.com/posts/13/image1.jpg"


@pytest.mark.count(post_storage=1, timeline=1)
@pytest.mark.usefixtures("insert_example_posts")
def test_get_posts_no_posts(client):
    response = client.get("/api/posts/?start=0&count=0")
    assert response.status_code == 200
    response_content = response.json()
    assert response_content["links"] == {
        "self": "http://microblog.com/posts?start=0&count=0",
        "next": "http://microblog.com/posts?start=0&count=0",
    }
    assert response_content["data"] == []


@pytest.mark.count(post_storage=1, timeline=1)
@pytest.mark.usefixtures("insert_example_posts")
def test_get_posts_from_timeline_and_storage(client):
    response = client.get("/api/posts/?start=0&count=2")
    assert response.status_code == 200
    response_content = response.json()
    check_get_posts_response(response_content)


@pytest.mark.count(timeline=2)
@pytest.mark.usefixtures("insert_example_posts")
def test_get_posts_from_timeline_only(client):
    response = client.get("/api/posts/?start=0&count=2")
    response_content = response.json()
    data = response_content["data"]
    assert len(data) == 2


def test_get_posts_not_enough_posts(client):
    response = client.get("/api/posts/?start=0&count=999")
    response_content = response.json()
    data = response_content["data"]
    assert len(data) == 0


@pytest.mark.asyncio
async def test_get_and_add_post(client):
    token = signup_user(client)["token"]
    response = client.post("/api/posts/", json=ADD_POST_REQUEST,
                           cookies={"token": token})
    assert response.status_code == 200
    assert response.json() == {"id": "0"}

    response = client.get("/api/posts/?start=0&count=2")
    assert response.status_code == 200
    response_content = response.json()
    check_get_posts_response(response_content, check_date=False)


@pytest.mark.asyncio
async def test_add_and_get_post_from_timeline_only(client, monkeypatch):
    token = signup_user(client)["token"]
    response = client.post("/api/posts/", json=ADD_POST_REQUEST,
                           cookies={"token": token})
    assert response.status_code == 200

    monkeypatch.setattr(client.app, "post_storage", None)

    response = client.get("/api/posts/?start=0&count=1")
    assert response.status_code == 200
    check_get_posts_response(response.json(), check_date=False)


def test_add_and_get_post_from_timeline_and_post_storage(client):
    token = signup_user(client)["token"]
    response = client.post("/api/posts/", json=ADD_POST_REQUEST,
                           cookies={"token": token})
    assert response.status_code == 200

    response = client.get("/api/posts/?start=0&count=2")
    assert response.status_code == 200
    data = response.json()["data"]

    assert len(data) == 2
    assert data[0]["id"] == data[1]["id"]


@pytest.mark.asyncio
async def test_add_post_invalid_type(client):
    token = signup_user(client)["token"]
    body = {"data": {"type": "bananas"}}
    response = client.post("/api/posts/", json=body,
                           cookies={"token": token})
    assert response.status_code == 400


def test_get_datetime_str_zero_microseconds():
    d = datetime(1000, 1, 1, 1, 1, 1, microsecond=0)
    s = posts.get_datetime_str(d)
    assert len(s) == 24
    assert s[-4:-1] == "000"


def test_get_datetime_str_too_big_precision():
    d = datetime(1000, 1, 1, 1, 1, 1, microsecond=999)
    s = posts.get_datetime_str(d)
    assert len(s) == 24
    assert s[-4:-1] == "000"


def test_get_datetime_str_good_precision():
    d = datetime(1000, 1, 1, 1, 1, 1, microsecond=234000)
    s = posts.get_datetime_str(d)
    assert len(s) == 24
    assert s[-4:-1] == "234"
