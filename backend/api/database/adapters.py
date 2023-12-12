from backend.domain.entities import Post, Timeline, User, Media
from backend.domain import gateways
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCursor
import datetime


async def cursor_to_posts(cursor: AsyncIOMotorCursor) -> list[Post]:
    posts = []
    for p in await cursor.to_list(None):
        attributes = p["attributes"]
        author = attributes["author"]
        media = attributes["media"]
        posts.append(
            Post(
                id=str(p["_id"]),
                text=attributes["text"],
                author=User(author["id"], author["attributes"]["name"]),
                media=[
                    Media(Media.Type[m["type"].upper()], m["src"])
                    for m in media
                ],
                date=datetime.datetime.strptime(
                    attributes["created"], "%Y-%m-%d %H:%M:%S.%f"
                ),
            )
        )
    return posts


def post_to_doc(post: Post):
    author = {
        "id": post.author.id,
        "attributes": {
            "name": post.author.name,
            "avatar": {
                "src": f"http://microblog.com/avatars/{post.author.name}.png"
            },
        },
    }
    datetime_str = post.datetime.strftime("%Y-%m-%d %H:%M:%S.%f")
    post_doc = {
        "type": "posts",
        "attributes": {
            "author": author,
            "text": post.text,
            "created": datetime_str,
            "media": [
                {
                    "type": m.type.name.lower(),
                    "src": m.src,
                }
                for m in post.media
            ],
        },
    }
    return post_doc


class PostStorageDatabase(gateways.PostStorageInterface):
    def __init__(self, db: AsyncIOMotorDatabase) -> None:
        self.db = db

    async def add_post(self, post: Post) -> Post:
        await self.db["posts"].insert_one(post_to_doc(post))

    async def get_any_posts(self, count) -> list[Post]:
        cursor: AsyncIOMotorCursor = self.db["posts"].find(limit=count)
        posts = await cursor_to_posts(cursor)
        return posts


TIMELINE_CAPACITY = 10


class TimelineStorageDatabase(gateways.TimelineStorageInterface):
    def __init__(self, db: AsyncIOMotorDatabase) -> None:
        self.db = db

    async def read(self) -> Timeline:
        timeline = Timeline(TIMELINE_CAPACITY)
        cursor = self.db["timeline"].find()
        posts = await cursor_to_posts(cursor)
        timeline.init_posts(posts)
        return timeline

    async def write(self, timeline: Timeline):
        pass
