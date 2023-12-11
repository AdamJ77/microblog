def test_get_posts_no_posts(client):
    response = client.get("/posts/?start=0&count=0")
    assert response.status_code == 200
    response_content = response.json()
    assert response_content["links"] == {
        "self": "http://microblog.com/posts?start=0&count=0",
        "next": "http://microblog.com/posts?start=0&count=0",
    }
    assert response_content["data"] == []


def test_get_posts_two_posts(client):
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
