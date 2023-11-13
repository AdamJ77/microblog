from backend.domain.entities import Post
from backend.domain.gateways import (
    PostStorageInterface,
    TimelineStorageInterface
)


def add_post(
        post_storage: PostStorageInterface,
        timeline_storage: TimelineStorageInterface,
        post: Post):
    post_storage.add_post(post)
    timeline = timeline_storage.read()
    timeline.try_add_post(post)
    timeline_storage.write(timeline)


def get_subset_of_posts(
        post_storage: PostStorageInterface,
        timeline_storage: TimelineStorageInterface,
        count):
    timeline_posts = timeline_storage.read().posts
    if len(timeline_posts) >= count:
        return timeline_posts[:count]

    posts_left = count - len(timeline_posts)
    main_storage_posts = post_storage.get_any_posts(posts_left)
    return timeline_posts + main_storage_posts
