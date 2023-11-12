from domain.entities import Post
from domain.gateways import PostRepoInterface, TimelineStorageInterface


def add_post(
        repo: PostRepoInterface,
        timeline_storage: TimelineStorageInterface,
        post: Post):
    repo.add_post(post)
    timeline = timeline_storage.read()
    timeline.try_add_post(post)
    timeline_storage.write(timeline)


def get_subset_of_posts(
        repo: PostRepoInterface,
        timeline_storage: TimelineStorageInterface,
        count):
    timeline_posts = timeline_storage.read().get_all_posts()
    if len(timeline_posts) >= count:
        return timeline_posts[:count]
    repo_posts = repo.get_any_posts(count - len(timeline_posts))
    return timeline_posts + repo_posts
