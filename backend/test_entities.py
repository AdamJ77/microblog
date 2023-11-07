from entities import Post


def test_post_instantiation():
    text = 'Bajojajo'
    post = Post(text)
    assert post.text == text
