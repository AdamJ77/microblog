from fastapi import APIRouter


router = APIRouter(
    prefix='/posts',
    tags=['Posts'],
)



@router.get('/')
async def get_posts(
    start: int,
    count: int
):
    # TODO: getting the posts
    pass
