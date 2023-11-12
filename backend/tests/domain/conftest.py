import pytest


@pytest.fixture
def timeline():
    from domain import gateways

    class FakeTimeline(gateways.TimelineInterface):
        def __init__(self) -> None:
            self.posts = []

        def add_post(self, post):
            self.posts.append(post)

        def get_all_posts(self):
            return self.posts

    return FakeTimeline()
