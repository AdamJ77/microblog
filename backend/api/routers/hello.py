from fastapi import APIRouter
from starlette.requests import Request

from backend.api.logger import LoggingRoute


router = APIRouter(
    route_class=LoggingRoute,
    prefix='/hello',
    tags=['Hello']
)


@router.get('/')
async def get_hello(request: Request):
    db = request.app.database
    inserted_id = (await db['hello'].insert_one({'foo': 'Hello world!'})).inserted_id
    foo_data = (await db['hello'].find_one({'_id': inserted_id}))['foo']
    return {'msg': foo_data}
