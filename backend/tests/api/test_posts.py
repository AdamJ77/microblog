def test_get_posts_no_posts(client):
    response = client.get("/posts/?start=0&count=0")
    assert response.status_code == 200
    response_content = response.json()
    assert response_content["links"] == {
        "self": "http://microblog.com/posts?start=0&count=0",
        "next": "http://microblog.com/posts?start=0&count=0",
    }
    assert response_content["data"] == []
