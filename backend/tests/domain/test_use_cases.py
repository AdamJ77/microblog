from domain.entities import Post
from domain import use_cases
from domain.gateways import PostRepoInterface, TimelineStorageInterface


def test_add_post(
        repo: PostRepoInterface,
        timeline_storage: TimelineStorageInterface,
        post: Post):
    assert len(repo.get_all_posts()) == 0
    assert len(timeline_storage.read().get_all_posts()) == 0

    use_cases.add_post(repo, timeline_storage, post)

    assert len(repo.get_all_posts()) == 1
    assert len(timeline_storage.read().get_all_posts()) == 1


def test_get_subset_of_posts(repo: PostRepoInterface, post):
    repo.add_post(post)
    repo.add_post(post)

    result = use_cases.get_subset_of_posts(repo, 1)
    assert len(result) == 1
    assert result[0].text == "Bajojajo"

    result = use_cases.get_subset_of_posts(repo, 2)
    assert len(result) == 2
