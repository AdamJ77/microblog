from backend.api.database import adapters


def test_post_to_doc(post):
    post_doc = adapters.post_to_doc(post)
    assert post_doc["type"] == "posts"
    attributes = post_doc["attributes"]

    author = attributes["author"]
    assert author["id"] == "213"
    assert author["attributes"]["name"] == "Greg"
    assert (
        author["attributes"]["avatar"]["src"]
        == "http://microblog.com/avatars/Greg.png"
    )

    assert attributes["text"] == "Bajojajo"
    assert attributes["created"] == "1970-01-01 00:00:00.000000"

    assert len(attributes["media"]) == 1
    media = attributes["media"][0]
    assert media["type"] == "image"
    assert media["src"] == "http://microblog.com/posts/13/image1.jpg"
