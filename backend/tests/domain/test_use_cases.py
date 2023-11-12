from domain.entities import Post
from domain import use_cases
from domain.gateways import PostRepoInterface, TimelineInterface


def test_add_post(
        repo: PostRepoInterface,
        timeline: TimelineInterface,
        post: Post):
    assert len(repo.get_all_posts()) == 0
    assert len(timeline.get_all_posts()) == 0

    use_cases.add_post(repo, timeline, post)

    assert len(repo.get_all_posts()) == 1
    assert len(timeline.get_all_posts()) == 1


def test_get_all_posts_no_posts(
        repo: PostRepoInterface,
        timeline: TimelineInterface):
    result = use_cases.get_all_posts(repo, timeline)
    assert len(result) == 0


def test_get_all_posts_one_post(
        repo: PostRepoInterface,
        timeline: TimelineInterface,
        post: Post):
    repo.add_post(post)
    result = use_cases.get_all_posts(repo, timeline)
    assert len(result) == 1


def test_get_subset_of_posts(repo: PostRepoInterface, post):
    repo.add_post(post)
    repo.add_post(post)

    result = use_cases.get_subset_of_posts(repo, 1)
    assert len(result) == 1
    assert result[0].text == "Bajojajo"

    result = use_cases.get_subset_of_posts(repo, 2)
    assert len(result) == 2
