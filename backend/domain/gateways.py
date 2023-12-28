from abc import ABC
from backend.domain.entities import Post, Timeline


class PostStorageInterface(ABC):
    async def add_post(self, post: Post) -> Post:
        pass

    # Should not return the same posts on each call
    async def get_any_posts(self, count) -> list[Post]:
        pass


class TimelineStorageInterface(ABC):
    async def read(self) -> Timeline:
        pass

    async def write(self, timeline: Timeline):
        pass
