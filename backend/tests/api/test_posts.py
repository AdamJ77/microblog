from backend.api.routers import posts
from pymongo.collection import Collection
from datetime import datetime

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


def insert_example_post(collection: Collection, post, count=1):
    from backend.api.database.adapters import post_to_doc

    post_doc = post_to_doc(post)
    for _ in range(count):
        collection.insert_one(post_doc.copy())


def test_get_posts_no_posts(client, db, post):
    insert_example_post(db["posts"], post)
    insert_example_post(db["timeline"], post)

    response = client.get("/posts/?start=0&count=0")
    assert response.status_code == 200
    response_content = response.json()
    assert response_content["links"] == {
        "self": "http://microblog.com/posts?start=0&count=0",
        "next": "http://microblog.com/posts?start=0&count=0",
    }
    assert response_content["data"] == []


def check_get_posts_response(response, check_date=True):
    assert response["links"]["self"]
    assert response["links"]["next"]

    for post in response["data"]:
        assert post["type"] == "posts"

        avatar_src = "http://microblog.com/users/avatars/Greg.png"
        author = post["attributes"]["author"]
        assert author["id"] == "213"
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


def test_get_posts_from_timeline_and_storage(client, db, post):
    insert_example_post(db["posts"], post)
    insert_example_post(db["timeline"], post)

    response = client.get("/posts/?start=0&count=2")
    assert response.status_code == 200
    response_content = response.json()
    check_get_posts_response(response_content)


def test_get_posts_from_timeline_only(client, db, post):
    insert_example_post(db["timeline"], post, 2)
    response = client.get("/posts/?start=0&count=2")
    response_content = response.json()
    data = response_content["data"]
    assert len(data) == 2


def test_get_posts_not_enough_posts(client):
    response = client.get("/posts/?start=0&count=999")
    response_content = response.json()
    data = response_content["data"]
    assert len(data) == 0


def test_get_and_add_post(client):
    response = client.post("/posts/", json=ADD_POST_REQUEST)
    assert response.status_code == 200
    assert response.json() == {"id": "0"}

    response = client.get("/posts/?start=0&count=2")
    assert response.status_code == 200
    response_content = response.json()
    check_get_posts_response(response_content, check_date=False)


def test_add_and_get_post_from_timeline_only(client, monkeypatch):
    response = client.post("/posts/", json=ADD_POST_REQUEST)
    assert response.status_code == 200

    # Ensure that posts cannot be retrieved from post storage (timeline only)
    monkeypatch.setattr(client.app, "post_storage", None)

    response = client.get("/posts/?start=0&count=1")
    assert response.status_code == 200
    check_get_posts_response(response.json(), check_date=False)


def test_add_post_invalid_type(client):
    body = {"data": {"type": "bananas"}}
    response = client.post("/posts/", json=body)
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
