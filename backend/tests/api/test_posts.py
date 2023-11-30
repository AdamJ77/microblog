def test_get_posts_no_posts(client):
    response = client.get("/posts/?start=0&count=1")
    assert response.status_code == 200
    assert response.json() == {
        "links": {
            "self": "http://microblog.com/posts?start=0&count=1",
            "next": "http://microblog.com/posts?start=1&count=1",
        },
        "data": [],
    }
