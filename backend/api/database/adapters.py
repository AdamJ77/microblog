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
                author=User(author["id"], author["attributes"]["name"],
                            author["attributes"]["avatar"]),
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
                "src": post.author.avatar
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
    if post.id is not None:
        post_doc["_id"] = post.id
    return post_doc


class PostStorageDatabase(gateways.PostStorageInterface):
    def __init__(self, db: AsyncIOMotorDatabase) -> None:
        self.db = db

    async def add_post(self, post: Post) -> str:
        id = (await self.db["posts"].insert_one(post_to_doc(post))).inserted_id
        return id

    async def get_any_posts(self, count) -> list[Post]:
        cursor: AsyncIOMotorCursor = self.db["posts"].find(limit=count)
        posts = await cursor_to_posts(cursor)
        return posts


class TimelineStorageDatabase(gateways.TimelineStorageInterface):
    timeline_capacity = 10

    def __init__(self, db: AsyncIOMotorDatabase) -> None:
        self.db = db

    async def read(self) -> Timeline:
        timeline = Timeline(self.timeline_capacity)
        cursor = self.db["timeline"].find()
        posts = await cursor_to_posts(cursor)
        timeline.init_posts(posts)
        return timeline

    async def write(self, timeline: Timeline):
        await self.db["timeline"].delete_many(filter={})  # Delete all
        await self.db["timeline"].insert_many(
            [post_to_doc(p) for p in timeline.posts]
        )
