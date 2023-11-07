from gateways import PostRepoInterface


def get_all_posts_use_case(repo: PostRepoInterface):
    return repo.get_all_posts()
