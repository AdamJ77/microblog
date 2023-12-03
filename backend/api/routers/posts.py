from fastapi import APIRouter
from backend.domain import use_cases, gateways

AVATAR_BASE_URL = "http://microblog.com/users/avatars/"

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


class PostStorageAdapter(gateways.PostStorageInterface):
    pass


class TimelineStorageAdapter(gateways.TimelineStorageInterface):
    pass


db = PostStorageAdapter()
timeline = TimelineStorageAdapter()


@router.get("/")
async def get_posts(start: int, count: int):
    next = start + count
    posts = use_cases.get_subset_of_posts(db, timeline, count)
    data = []
    for p in posts:
        author = {
            "id": p.author.id,
            "attributes": {
                "name": p.author.name,
                "avatar": {"src": AVATAR_BASE_URL + p.author.name + ".png"},
            },
        }
        datetime = (
            str(p.datetime.date()) + "T" + str(p.datetime.time()) + ".000Z"
        )
        media = [{"type": m.type.name.lower(), "src": m.src} for m in p.media]
        data.append(
            {
                "id": p.id,
                "type": "posts",
                "attributes": {
                    "author": author,
                    "body": p.text,
                    "created": datetime,
                    "media": media,
                },
            }
        )
    return {
        "links": {
            "self": f"http://microblog.com/posts?start={start}&count={count}",
            "next": f"http://microblog.com/posts?start={next}&count={count}",
        },
        "data": data,
    }
