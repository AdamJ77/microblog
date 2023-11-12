from abc import ABC
from backend.domain.entities import Post, Timeline


class PostStorageInterface(ABC):
    def add_post(self, post: Post) -> Post:
        pass

    # Should not return the same posts on each call
    def get_any_posts(self, count) -> list[Post]:
        pass


class TimelineStorageInterface(ABC):
    def read(self) -> Timeline:
        pass

    def write(self, timeline: Timeline):
        pass
