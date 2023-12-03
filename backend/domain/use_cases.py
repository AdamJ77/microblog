from backend.domain.entities import Post
from backend.domain.gateways import (
    PostStorageInterface,
    TimelineStorageInterface,
)


def add_post(
    post_storage: PostStorageInterface,
    timeline_storage: TimelineStorageInterface,
    post: Post,
):
    post_storage.add_post(post)
    timeline = timeline_storage.read()
    timeline.try_add_post(post)
    timeline_storage.write(timeline)


def get_subset_of_posts(
    post_storage: PostStorageInterface,
    timeline_storage: TimelineStorageInterface,
    count,
    start=0,
):
    end = start + count
    posts = timeline_storage.read().posts
    if len(posts) >= end:
        return posts[start:end]

    posts_left = end - len(posts)
    posts.extend(post_storage.get_any_posts(posts_left))
    return posts[start:end]
