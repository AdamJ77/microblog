from backend.domain.entities import Post, Timeline
from backend.domain import use_cases
from backend.domain.gateways import (
    PostStorageInterface,
    TimelineStorageInterface,
)
import pytest


@pytest.mark.asyncio
async def test_add_post(
    post_storage: PostStorageInterface,
    timeline_storage: TimelineStorageInterface,
    post: Post,
):
    assert len(await post_storage.get_any_posts(10)) == 0
    assert len((await timeline_storage.read()).posts) == 0

    await use_cases.add_post(post_storage, timeline_storage, post)

    assert len(await post_storage.get_any_posts(10)) == 1
    assert len((await timeline_storage.read()).posts) == 1


@pytest.mark.asyncio
async def test_get_subset_of_posts_no_posts(
    post_storage: PostStorageInterface,
    timeline_storage: TimelineStorageInterface,
):
    result = await use_cases.get_subset_of_posts(
        post_storage, timeline_storage, start=0, count=10
    )
    assert len(result) == 0


@pytest.mark.asyncio
async def test_get_subset_of_posts_timeline_only(
    post_storage, timeline_storage, post
):
    await use_cases.add_post(post_storage, timeline_storage, post)

    result = await use_cases.get_subset_of_posts(
        None, timeline_storage, start=0, count=1
    )
    assert len(result) == 1

    with pytest.raises(AttributeError):
        await use_cases.get_subset_of_posts(
            None, timeline_storage, start=0, count=2
        )


@pytest.mark.asyncio
async def test_get_subset_of_posts_not_enough_in_timeline(
    post_storage: PostStorageInterface,
    timeline_storage: TimelineStorageInterface,
    post,
):
    await use_cases.add_post(post_storage, timeline_storage, post)
    await use_cases.add_post(post_storage, timeline_storage, post)

    result = await use_cases.get_subset_of_posts(
        post_storage, timeline_storage, start=0, count=2
    )
    assert len(result) == 2


@pytest.mark.asyncio
async def test_get_subset_of_posts_different_start(
    post_storage: PostStorageInterface,
    timeline_storage: TimelineStorageInterface,
    timeline: Timeline,
    posts,
):
    timeline.init_posts([posts["high priority"]])
    await timeline_storage.write(timeline)
    await post_storage.add_post(posts["low priority"])

    result1 = await use_cases.get_subset_of_posts(
        post_storage, timeline_storage, start=0, count=1
    )
    result2 = await use_cases.get_subset_of_posts(
        post_storage, timeline_storage, start=1, count=1
    )

    assert result1[0].text == "high"
    assert result2[0].text == "low"
