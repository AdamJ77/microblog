from app.entities import Post
from app.use_cases import get_all_posts_use_case, add_post_use_case
from app.gateways import PostRepoInterface


def test_add_post_use_case_add_one_post(repo: PostRepoInterface, post: Post):
    assert len(repo.get_all_posts()) == 0
    add_post_use_case(repo, post)
    assert len(repo.get_all_posts()) == 1


def test_get_all_posts_use_case_no_posts(repo: PostRepoInterface):
    result = get_all_posts_use_case(repo)
    assert len(result) == 0


def test_get_all_posts_use_case_one_post(repo: PostRepoInterface):
    repo.add_post(Post("Bajojajo"))
    result = get_all_posts_use_case(repo)
    assert len(result) == 1
