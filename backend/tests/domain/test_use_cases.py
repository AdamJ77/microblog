from backend.domain.entities import Post
from backend.domain import use_cases
from backend.domain.gateways import (
    PostStorageInterface,
    TimelineStorageInterface
)
import pytest


def test_add_post(
        post_storage: PostStorageInterface,
        timeline_storage: TimelineStorageInterface,
        post: Post):
    assert len(post_storage.get_any_posts(10)) == 0
    assert len(timeline_storage.read().posts) == 0

    use_cases.add_post(post_storage, timeline_storage, post)

    assert len(post_storage.get_any_posts(10)) == 1
    assert len(timeline_storage.read().posts) == 1


def test_get_subset_of_posts_no_posts(
        post_storage: PostStorageInterface,
        timeline_storage: TimelineStorageInterface,
        post):
    result = use_cases.get_subset_of_posts(post_storage, timeline_storage, 10)
    assert len(result) == 0


def test_get_subset_of_posts_timeline_only(
        post_storage,
        timeline_storage,
        post):
    use_cases.add_post(post_storage, timeline_storage, post)

    result = use_cases.get_subset_of_posts(None, timeline_storage, 1)
    assert len(result) == 1

    with pytest.raises(AttributeError):
        use_cases.get_subset_of_posts(None, timeline_storage, 2)


def test_get_subset_of_posts_not_enough_in_timeline(
        post_storage: PostStorageInterface,
        timeline_storage: TimelineStorageInterface,
        post):
    use_cases.add_post(post_storage, timeline_storage, post)
    use_cases.add_post(post_storage, timeline_storage, post)

    result = use_cases.get_subset_of_posts(post_storage, timeline_storage, 2)
    assert len(result) == 2
