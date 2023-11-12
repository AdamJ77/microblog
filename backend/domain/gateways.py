from abc import ABC
from domain.entities import Post


class PostRepoInterface(ABC):
    def add_post(self, post) -> Post:
        pass

    def get_all_posts(self) -> list[Post]:
        pass


class TimelineInterface(ABC):
    def add_post(self, post) -> Post:
        pass

    def get_all_posts(self) -> list[Post]:
        pass
