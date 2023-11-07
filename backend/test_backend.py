from entities import Post
from use_cases import get_all_posts_use_case
from gateways import PostRepoInterface


def test_post_instantiation():
    text = 'Bajojajo'
    post = Post(text)
    assert post.text == text


class FakePostRepo(PostRepoInterface):
    def __init__(self) -> None:
        self.posts = []

    def add_post(self, post: Post):
        self.posts.append(post)

    def get_all_posts(self):
        return self.posts


def test_get_post_use_case_no_posts():
    repo = FakePostRepo()
    result = get_all_posts_use_case(repo)
    assert len(result) == 0


def test_get_post_use_case_one_post():
    repo = FakePostRepo()
    repo.add_post(Post("Bajojajo"))
    result = get_all_posts_use_case(repo)
    assert len(result) == 1
