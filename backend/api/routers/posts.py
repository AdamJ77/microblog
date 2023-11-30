from fastapi import APIRouter


router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


@router.get("/")
async def get_posts(start: int, count: int):
    next = start + count
    return {
        "links": {
            "self": f"http://microblog.com/posts?start={start}&count={count}",
            "next": f"http://microblog.com/posts?start={next}&count={count}",
        },
        "data": [],
    }
