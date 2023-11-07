from abc import ABC
from entities import Post


class PostRepoInterface(ABC):
    def add_post(self, post) -> Post:
        pass

    def get_all_posts(self) -> list[Post]:
        pass
