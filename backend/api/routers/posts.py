from fastapi import APIRouter
from starlette.requests import Request
from backend.domain import use_cases

AVATAR_BASE_URL = "http://microblog.com/users/avatars/"

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
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
                "avatar": {"src": AVATAR_BASE_URL + p.author.name + ".png"},
            },
        }
        datetime = p.datetime.strftime(
            f"%Y-%m-%dT%H:%M:%S.{p.datetime.microsecond // 1000}Z"
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
