class Post:
    def __init__(self, text) -> None:
        self.text = text

    def get_text(self):
        return self.text


class User:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name
