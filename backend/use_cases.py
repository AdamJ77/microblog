from entities import Post
from gateways import PostRepoInterface


def add_post_use_case(repo: PostRepoInterface, post: Post):
    repo.add_post(post)


def get_all_posts_use_case(repo: PostRepoInterface):
    return repo.get_all_posts()
