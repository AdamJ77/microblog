import pytest
import copy
from backend.domain import entities, gateways


@pytest.fixture
def post_author():
    return entities.User(name='Author')


@pytest.fixture
def post(post_author):
    from datetime import datetime

    post_date = datetime.fromtimestamp(0)
    return entities.Post(
        text='Bajojajo',
        author=post_author,
        datetime=post_date)


@pytest.fixture
def posts(post_author):
    from datetime import datetime

    return {
        'low priority': entities.Post(
            text='low',
            author=post_author,
            datetime=datetime.fromtimestamp(0)),
        'high priority': entities.Post(
            text='high',
            author=post_author,
            datetime=datetime.fromtimestamp(999999))
    }


@pytest.fixture
def user():
    return entities.User(name='Maciej')


@pytest.fixture()
def post_storage():
    class FakePostStorage(gateways.PostStorageInterface):
        def __init__(self) -> None:
            self.posts = []

        def add_post(self, post: entities.Post):
            self.posts.append(post)

        def get_any_posts(self, count):
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

        def read(self) -> entities.Timeline:
            return copy.deepcopy(self.timeline)

        def write(self, timeline: entities.Timeline):
            self.timeline = copy.deepcopy(timeline)

    return FakeTimelineStorage()
