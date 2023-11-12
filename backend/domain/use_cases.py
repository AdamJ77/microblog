from domain.entities import Post, Timeline
from domain.gateways import PostRepoInterface


def add_post(
        repo: PostRepoInterface,
        timeline: Timeline,
        post: Post):
    repo.add_post(post)
    timeline.try_add_post(post)


def get_all_posts(
        repo: PostRepoInterface,
        timeline: Timeline):
    return repo.get_all_posts()


def get_subset_of_posts(repo: PostRepoInterface, count):
    return repo.get_all_posts()[:count]
