from datetime import datetime as dt


class Post:
    def __init__(self, text, author, datetime: dt = None) -> None:
        self.text = text
        self.author = author
        if datetime is None:
            datetime = dt.today()
        self.datetime = datetime

    def get_text(self):
        return self.text

    def get_author(self):
        return self.author

    def get_datetime(self):
        return self.datetime

    def get_priority(self):
        return (self.datetime - dt.today()).total_seconds()


class User:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name


class Timeline:
    def __init__(self, capacity) -> None:
        self.posts = []
        self.capacity = capacity

    def try_add_post(self, post):
        self.posts.append(post)
        self.posts.sort(key=lambda post: -post.get_priority())
        del self.posts[self.capacity:]

    def get_all_posts(self):
        return self.posts
