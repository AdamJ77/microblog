from domain.entities import Post
from domain import use_cases
from domain.gateways import PostRepoInterface, TimelineStorageInterface
import pytest


def test_add_post(
        repo: PostRepoInterface,
        timeline_storage: TimelineStorageInterface,
        post: Post):
    assert len(repo.get_any_posts(10)) == 0
    assert len(timeline_storage.read().get_all_posts()) == 0

    use_cases.add_post(repo, timeline_storage, post)

    assert len(repo.get_any_posts(10)) == 1
    assert len(timeline_storage.read().get_all_posts()) == 1


def test_get_subset_of_posts_no_posts(
        repo: PostRepoInterface,
        timeline_storage: TimelineStorageInterface,
        post):
    result = use_cases.get_subset_of_posts(repo, timeline_storage, 10)
    assert len(result) == 0


def test_get_subset_of_posts_timeline_only(repo, timeline_storage, post):
    use_cases.add_post(repo, timeline_storage, post)

    result = use_cases.get_subset_of_posts(None, timeline_storage, 1)
    assert len(result) == 1

    with pytest.raises(AttributeError):
        use_cases.get_subset_of_posts(None, timeline_storage, 2)


def test_get_subset_of_posts_not_enough_in_timeline(
        repo: PostRepoInterface,
        timeline_storage: TimelineStorageInterface,
        post):
    use_cases.add_post(repo, timeline_storage, post)
    use_cases.add_post(repo, timeline_storage, post)

    result = use_cases.get_subset_of_posts(repo, timeline_storage, 2)
    assert len(result) == 2
