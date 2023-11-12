import pytest


@pytest.fixture
def post_author():
    from domain import entities
    return entities.User(name='Author')


@pytest.fixture
def post(post_author):
    from domain.entities import Post
    from datetime import datetime
    post_date = datetime.fromtimestamp(0)
    return Post(text='Bajojajo', author=post_author, datetime=post_date)


@pytest.fixture
def user():
    from domain import entities
    return entities.User(name='Maciej')


@pytest.fixture()
def repo():
    from domain import entities, gateways

    class FakePostRepo(gateways.PostRepoInterface):
        def __init__(self) -> None:
            self.posts = []

        def add_post(self, post: entities.Post):
            self.posts.append(post)

        def get_all_posts(self):
            return self.posts
    return FakePostRepo()


@pytest.fixture
def timeline():
    from domain import entities

    return entities.Timeline(capacity=1)
