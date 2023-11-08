from fastapi.testclient import TestClient
from app import entities, gateways
import pytest


@pytest.fixture
def client() -> TestClient:
    from api.app import create_app

    app = create_app()
    return TestClient(app)


@pytest.fixture
def post_author():
    return entities.User(name='Author')


@pytest.fixture
def post(post_author):
    return entities.Post(text='Bajojajo', author=post_author)


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
