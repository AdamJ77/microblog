from abc import ABC
from domain.entities import Post, Timeline


class PostRepoInterface(ABC):
    def add_post(self, post: Post) -> Post:
        pass

    def get_all_posts(self) -> list[Post]:
        pass


class TimelineStorageInterface(ABC):
    def read(self) -> Timeline:
        pass

    def write(self, timeline: Timeline):
        pass
