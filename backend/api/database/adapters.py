from backend.domain.entities import Post, Timeline, User, Media
from backend.domain import gateways
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCursor
import datetime


class PostStorageDatabaseAdapter(gateways.PostStorageInterface):
    def __init__(self, db: AsyncIOMotorDatabase) -> None:
        self.db = db

    async def add_post(self, post: Post) -> Post:
        pass

    async def get_any_posts(self, count) -> list[Post]:
        cursor: AsyncIOMotorCursor = self.db["posts"].find(limit=count)
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


TIMELINE_CAPACITY = 10


class TimelineStorageDatabaseAdapter(gateways.TimelineStorageInterface):
    def __init__(self, db) -> None:
        self.db = db

    async def read(self) -> Timeline:
        return Timeline(TIMELINE_CAPACITY)

    async def write(self, timeline: Timeline):
        pass
