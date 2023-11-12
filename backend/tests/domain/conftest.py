import pytest
from domain import entities, gateways


@pytest.fixture
def post_author():
    return entities.User(name='Author')


@pytest.fixture
def post(post_author):
    from datetime import datetime

    post_date = datetime.fromtimestamp(0)
    return entities.Post(
        text='Bajojajo',
        author=post_author,
        datetime=post_date)


@pytest.fixture
def user():
    return entities.User(name='Maciej')


@pytest.fixture()
def repo():
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
    return entities.Timeline(capacity=1)
