from datetime import datetime


class User:
    def __init__(self, id, name) -> None:
        self.__id = id
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name


class Post:
    def __init__(self, id, text, author, date: datetime = None) -> None:
        self.__id = id
        self.__text = text
        self.__author = author
        self.__datetime = date or datetime.today()

    @property
    def id(self) -> int:
        return self.__id

    @property
    def text(self) -> str:
        return self.__text

    @property
    def author(self) -> User:
        return self.__author

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
        del self.__posts[self.__capacity:]

    @property
    def posts(self) -> list[Post]:
        return self.__posts
