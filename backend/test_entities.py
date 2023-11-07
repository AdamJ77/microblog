from entities import Post, User
import pytest


@pytest.fixture
def post():
    TEXT = 'Bajojajo'
    return Post(TEXT)


@pytest.fixture
def user():
    NAME = 'Maciej'
    return User(NAME)


def test_post_init(post: Post):
    assert post.get_text() == 'Bajojajo'


def test_user_init(user: User):
    assert user.get_name() == 'Maciej'
