from app.entities import Post, User


def test_post_init(post: Post):
    assert post.get_text() == 'Bajojajo'


def test_user_init(user: User):
    assert user.get_name() == 'Maciej'
