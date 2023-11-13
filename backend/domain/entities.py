from datetime import datetime as dt


class Post:
    def __init__(self, text, author, datetime: dt = None) -> None:
        self.__text = text
        self.__author = author
        if datetime is None:
            datetime = dt.today()
        self.__datetime = datetime

    @property
    def text(self):
        return self.__text

    @property
    def author(self):
        return self.__author

    @property
    def datetime(self):
        return self.__datetime

    @property
    def priority(self):
        return (self.datetime - dt.today()).total_seconds()


class User:
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name


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
    def posts(self):
        return self.__posts
