from backend.domain.entities import Post
from backend.domain.gateways import (
    PostStorageInterface,
    TimelineStorageInterface,
)


async def add_post(
    post_storage: PostStorageInterface,
    timeline_storage: TimelineStorageInterface,
    post: Post,
):
    id = await post_storage.add_post(post)
    post.id = str(id)
    timeline = await timeline_storage.read()
    timeline.try_add_post(post)
    await timeline_storage.write(timeline)


async def get_subset_of_posts(
    post_storage: PostStorageInterface,
    timeline_storage: TimelineStorageInterface,
    start,
    count,
):
    end = start + count
    posts = (await timeline_storage.read()).posts
    if len(posts) >= end:
        return posts[start:end]

    posts_left = end - len(posts)
    posts.extend(await post_storage.get_any_posts(posts_left))
    return posts[start:end]
