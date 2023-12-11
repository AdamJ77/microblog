from backend.api.routers import posts
from pymongo.collection import Collection
from datetime import datetime


def insert_example_post(collection: Collection, count):
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
    for _ in range(count):
        collection.insert_one(post.copy())


def test_get_posts_no_posts(client, db):
    insert_example_post(db["posts"], 1)
    insert_example_post(db["timeline"], 1)

    response = client.get("/posts/?start=0&count=0")
    assert response.status_code == 200
    response_content = response.json()
    assert response_content["links"] == {
        "self": "http://microblog.com/posts?start=0&count=0",
        "next": "http://microblog.com/posts?start=0&count=0",
    }
    assert response_content["data"] == []


def test_get_posts_from_timeline_and_storage(client, db):
    insert_example_post(db["posts"], 1)
    insert_example_post(db["timeline"], 1)

    response = client.get("/posts/?start=0&count=2")
    assert response.status_code == 200
    response_content = response.json()
    assert response_content["links"] == {
        "self": "http://microblog.com/posts?start=0&count=2",
        "next": "http://microblog.com/posts?start=2&count=2",
    }

    data = response_content["data"]
    assert len(data) == 2

    for post in data:
        assert post["type"] == "posts"

        avatar_src = "http://microblog.com/users/avatars/Greg.png"
        author = post["attributes"]["author"]
        assert author["id"] == "213"
        assert author["attributes"]["name"] == "Greg"
        assert author["attributes"]["avatar"]["src"] == avatar_src

        assert post["attributes"]["body"] == "Bajojajo"
        assert post["attributes"]["created"] == "2023-04-20T18:34:59.213Z"

        media = post["attributes"]["media"]
        for m in media:
            assert m["type"] == "image"
            assert m["src"] == "http://microblog.com/posts/13/image1.jpg"


def test_get_posts_from_timeline_only(client, db):
    insert_example_post(db["timeline"], 2)
    response = client.get("/posts/?start=0&count=2")
    response_content = response.json()
    data = response_content["data"]
    assert len(data) == 2


def test_get_posts_not_enough_posts(client, db):
    insert_example_post(db["posts"], 1)
    insert_example_post(db["timeline"], 1)
    response = client.get("/posts/?start=0&count=999")
    response_content = response.json()
    data = response_content["data"]
    assert len(data) == 2


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
