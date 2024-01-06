from datetime import datetime
from enum import Enum, auto


class Media:
    class Type(Enum):
        IMAGE = auto()
        VIDEO = auto()

    def __init__(self, type, src) -> None:
        self.__type = type
        self.__src = src

    @property
    def type(self) -> Type:
        return self.__type

    @property
    def src(self) -> str:
        return self.__src


class User:
    def __init__(self, id, name, avatar) -> None:
        self.__id = id
        self.__name = name
        self.__avatar = avatar

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def avatar(self) -> str:
        return self.__avatar


class Post:
    def __init__(
        self, id, text, author, media=None, date: datetime = None
    ) -> None:
        self.__id = id
        self.__text = text
        self.__author = author
        self.__media = media or []
        self.__datetime = date or datetime.today()

    @property
    def id(self) -> str:
        return self.__id

    @property
    def text(self) -> str:
        return self.__text

    @property
    def author(self) -> User:
        return self.__author

    @property
    def media(self) -> list[Media]:
        return self.__media

    @property
    def datetime(self) -> datetime:
        return self.__datetime

    @property
    def priority(self) -> float:
        return (self.datetime - datetime.today()).total_seconds()


class Timeline:
    def __init__(self, capacity) -> None:
        self.__posts = []
        self.__capacity = capacity

    def init_posts(self, posts: list[Post]):
        self.__posts.extend(posts)
        self.__truncate()

    def try_add_post(self, post):
        self.__posts.append(post)
        self.__truncate()

    def __truncate(self):
        self.__posts.sort(key=lambda post: -post.priority)
        truncate_start = self.__capacity
        del self.__posts[truncate_start:]

    @property
    def posts(self) -> list[Post]:
        return self.__posts
