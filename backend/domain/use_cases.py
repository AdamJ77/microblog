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


def get_subset_of_posts(repo: PostRepoInterface, count):
    return repo.get_all_posts()[:count]
