from domain.entities import Post
from domain.gateways import PostRepoInterface, TimelineInterface


def add_post(
        repo: PostRepoInterface,
        timeline: TimelineInterface,
        post: Post):
    repo.add_post(post)
    timeline.add_post(post)


def get_all_posts(
        repo: PostRepoInterface,
        timeline: TimelineInterface):
    return repo.get_all_posts()


def get_subset_of_posts(repo: PostRepoInterface, count):
    return repo.get_all_posts()[:count]
