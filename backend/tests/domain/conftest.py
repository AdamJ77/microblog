import pytest
import copy
from backend.domain import entities, gateways


@pytest.fixture
def posts(post_author):
    from datetime import datetime

    return {
        "low priority": entities.Post(
            id=0,
            text="low",
            author=post_author,
            date=datetime.utcfromtimestamp(0),
        ),
        "high priority": entities.Post(
            id=1,
            text="high",
            author=post_author,
            date=datetime.utcfromtimestamp(999999),
        ),
    }


@pytest.fixture
def user():
    return entities.User(id=0, name="Maciej",
                         avatar="http://microblog.com/avatars/Greg.png")


@pytest.fixture()
def post_storage():
    class FakePostStorage(gateways.PostStorageInterface):
        def __init__(self) -> None:
            self.posts = []

        async def add_post(self, post: entities.Post):
            self.posts.append(post)

        async def get_any_posts(self, count):
            return self.posts[:count]

    return FakePostStorage()


@pytest.fixture
def timeline():
    return entities.Timeline(capacity=1)


@pytest.fixture
def timeline_storage(timeline):
    class FakeTimelineStorage(gateways.TimelineStorageInterface):
        def __init__(self) -> None:
            self.timeline = timeline

        async def read(self) -> entities.Timeline:
            return copy.deepcopy(self.timeline)

        async def write(self, timeline: entities.Timeline):
            self.timeline = copy.deepcopy(timeline)

    return FakeTimelineStorage()
