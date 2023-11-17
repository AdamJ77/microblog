from backend.domain.entities import Post, User, Timeline
from datetime import datetime
from freezegun import freeze_time


ZERO_TIMESTAMP = "1970-01-01 00:00:00"


def test_post_get_text(post: Post):
    assert post.text == 'Bajojajo'


def test_post_get_author(post: Post, post_author: User):
    assert post.author == post_author


def test_post_get_datetime(post: Post):
    assert post.datetime == datetime.fromtimestamp(0)


@freeze_time(ZERO_TIMESTAMP)
def test_post_get_current_datetime(post_author):
    post = Post("", post_author)
    assert post.datetime == datetime.fromtimestamp(0)


@freeze_time(ZERO_TIMESTAMP)
def test_post_get_priority_zero_timestamp():
    post = Post("", None, datetime.fromtimestamp(0))
    assert post.priority == 0


@freeze_time(ZERO_TIMESTAMP)
def test_post_get_priority_one_hour_timestamp():
    post = Post("", None, datetime.fromtimestamp(-3600))
    assert post.priority == -3600


def test_user_get_name(user: User):
    assert user.name == 'Maciej'


def test_timeline_init_posts(timeline: Timeline, posts: dict):
    post_list = list(posts.values())
    timeline.init_posts(post_list)

    assert len(timeline.posts) == 1


def test_timeline_add_and_get_post(timeline: Timeline, post):
    timeline.try_add_post(post)
    assert timeline.posts == [post]


def test_timeline_overflow(timeline: Timeline, posts):
    timeline.try_add_post(posts['low priority'])
    assert timeline.posts == [posts['low priority']]

    timeline.try_add_post(posts['high priority'])
    assert timeline.posts == [posts['high priority']]
