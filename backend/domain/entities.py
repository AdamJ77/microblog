class Post:
    def __init__(self, text, author) -> None:
        self.text = text
        self.author = author

    def get_text(self):
        return self.text

    def get_author(self):
        return self.author


class User:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name
