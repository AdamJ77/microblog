from domain.entities import Post, User, Timeline
from datetime import datetime
from freezegun import freeze_time


ZERO_TIMESTAMP = "1970-01-01 00:00:00"


def test_post_get_text(post: Post):
    assert post.get_text() == 'Bajojajo'


def test_post_get_author(post: Post, post_author: User):
    assert post.get_author() == post_author


def test_post_get_datetime(post: Post):
    assert post.get_datetime() == datetime.fromtimestamp(0)


@freeze_time(ZERO_TIMESTAMP)
def test_post_get_current_datetime(post_author):
    post = Post("", post_author)
    assert post.get_datetime() == datetime.fromtimestamp(0)


@freeze_time(ZERO_TIMESTAMP)
def test_post_get_priority_zero_timestamp():
    post = Post("", None, datetime.fromtimestamp(0))
    assert post.get_priority() == 0


@freeze_time(ZERO_TIMESTAMP)
def test_post_get_priority_one_hour_timestamp():
    post = Post("", None, datetime.fromtimestamp(-3600))
    assert post.get_priority() == -3600


def test_user_get_name(user: User):
    assert user.get_name() == 'Maciej'


def test_timeline_add_and_get_post(timeline: Timeline, post):
    timeline.try_add_post(post)
    assert timeline.get_all_posts() == [post]


def test_timeline_add_two_posts_with_capacity_1(timeline: Timeline, post):
    timeline.try_add_post(post)
    timeline.try_add_post(post)
    assert timeline.get_all_posts() == [post]
