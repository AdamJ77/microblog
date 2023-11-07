from entities import Post
from use_cases import get_all_posts_use_case, add_post_use_case
from gateways import PostRepoInterface
import pytest


@pytest.fixture()
def repo():
    class FakePostRepo(PostRepoInterface):
        def __init__(self) -> None:
            self.posts = []

        def add_post(self, post: Post):
            self.posts.append(post)

        def get_all_posts(self):
            return self.posts
    return FakePostRepo()


@pytest.fixture
def post():
    TEXT = 'Bajojajo'
    return Post(TEXT)


def test_add_post_use_case_add_one_post(repo: PostRepoInterface, post: Post):
    assert len(repo.get_all_posts()) == 0
    add_post_use_case(repo, post)
    assert len(repo.get_all_posts()) == 1


def test_get_post_use_case_no_posts(repo: PostRepoInterface):
    result = get_all_posts_use_case(repo)
    assert len(result) == 0


def test_get_post_use_case_one_post(repo: PostRepoInterface):
    repo.add_post(Post("Bajojajo"))
    result = get_all_posts_use_case(repo)
    assert len(result) == 1
