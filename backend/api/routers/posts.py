from fastapi import APIRouter, HTTPException, Depends
from starlette.requests import Request

from backend.api.logger import LoggingRoute
from backend.domain import use_cases
from backend.api.routers.auth import get_current_user
from bson import ObjectId

AVATAR_BASE_URL = "http://microblog.com/users/avatars/"

router = APIRouter(
    route_class=LoggingRoute,
    prefix="/posts",
    tags=["Posts"],
)


def get_datetime_str(datetime):
    return datetime.strftime(
        f"%Y-%m-%dT%H:%M:%S.{datetime.microsecond // 1000:03}Z"
    )


@router.get("/")
async def get_posts(request: Request, start: int, count: int):
    next = start + count
    posts = await use_cases.get_subset_of_posts(
        request.app.post_storage,
        request.app.timeline,
        start=start,
        count=count,
    )
    data = []
    for p in posts:
        author = {
            "id": p.author.id,
            "attributes": {
                "name": p.author.name,
                "avatar": {"src": p.author.avatar["src"]},
            },
        }
        datetime = get_datetime_str(p.datetime)
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


@router.post("/")
async def add_post(request: Request, user_id: str = Depends(get_current_user)):
    from backend.domain.entities import Post, User, Media
    from datetime import datetime

    body = await request.json()
    data = body["data"]
    if data["type"] != "posts":
        raise HTTPException(
            status_code=400, detail=f"Invalid item type: {data['type']}"
        )

    db = request.app.database
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    name = user.get("username", "")
    avatar = user.get("avatar", "")
    author = User(user_id, name, avatar)

    media = [
        Media(Media.Type[m["type"].upper()], m["src"])
        for m in data["attributes"]["media"]
    ]
    post = Post(
        id=None,
        text=data["attributes"]["body"],
        author=author,
        media=media,
        date=datetime.now(),
    )
    await use_cases.add_post(
        request.app.post_storage, request.app.timeline, post
    )
    return {"id": "0"}
