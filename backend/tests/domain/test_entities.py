from domain.entities import Post, User


def test_post_get_text(post: Post):
    assert post.get_text() == 'Bajojajo'


def test_post_get_author(post: Post, post_author: User):
    assert post.get_author() == post_author


def test_user_init(user: User):
    assert user.get_name() == 'Maciej'
