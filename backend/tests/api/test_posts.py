from backend.domain.entities import User, Post, Timeline, Media
from backend.api.routers.posts import db, timeline
import pytest


@pytest.fixture
def post_author():
    return User(id=0, name="Author")


@pytest.fixture
def post(post_author):
    from datetime import datetime

    post_date = datetime.fromtimestamp(0)
    return Post(
        id=0,
        text="Bajojajo",
        author=post_author,
        media=[
            Media(Media.Type.IMAGE, "http://microblog.com/posts/13/image1.jpg")
        ],
        date=post_date,
    )


@pytest.fixture
def mock_db_and_timeline(monkeypatch, post):
    def mock_get_any_posts(count) -> list[Post]:
        return [post]

    def mock_read() -> Timeline:
        t = Timeline(10)
        t.init_posts([post])
        return t

    monkeypatch.setattr(db, "get_any_posts", mock_get_any_posts)
    monkeypatch.setattr(timeline, "read", mock_read)


def test_get_posts_no_posts(client, mock_db_and_timeline):
    response = client.get("/posts/?start=0&count=0")
    assert response.status_code == 200
    response_content = response.json()
    assert response_content["links"] == {
        "self": "http://microblog.com/posts?start=0&count=0",
        "next": "http://microblog.com/posts?start=0&count=0",
    }
    assert response_content["data"] == []


def test_get_posts_two_posts(client, mock_db_and_timeline):
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
        assert post["id"] == 0
        assert post["type"] == "posts"

        avatar_src = "http://microblog.com/users/avatars/Author.png"
        author = post["attributes"]["author"]
        assert author["id"] == 0
        assert author["attributes"]["name"] == "Author"
        assert author["attributes"]["avatar"]["src"] == avatar_src

        assert post["attributes"]["body"] == "Bajojajo"
        assert post["attributes"]["created"] == "1970-01-01T01:00:00.000Z"

        media = post["attributes"]["media"]
        for m in media:
            assert m["type"] == "image"
            assert m["src"] == "http://microblog.com/posts/13/image1.jpg"
