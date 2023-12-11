from backend.domain.entities import Post, Timeline, User, Media
from backend.domain import gateways
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCursor
import datetime


async def build_posts(cursor: AsyncIOMotorCursor) -> list[Post]:
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
                    attributes["created"], "%Y-%m-%dT%H:%M:%S.%fZ"
                ),
            )
        )
    return posts


class PostStorageDatabase(gateways.PostStorageInterface):
    def __init__(self, db: AsyncIOMotorDatabase) -> None:
        self.db = db

    async def add_post(self, post: Post) -> Post:
        pass

    async def get_any_posts(self, count) -> list[Post]:
        cursor: AsyncIOMotorCursor = self.db["posts"].find(limit=count)
        posts = await build_posts(cursor)
        return posts


TIMELINE_CAPACITY = 10


class TimelineStorageDatabase(gateways.TimelineStorageInterface):
    def __init__(self, db: AsyncIOMotorDatabase) -> None:
        self.db = db

    async def read(self) -> Timeline:
        timeline = Timeline(TIMELINE_CAPACITY)
        cursor = self.db["timeline"].find()
        posts = await build_posts(cursor)
        timeline.init_posts(posts)
        return timeline

    async def write(self, timeline: Timeline):
        pass
