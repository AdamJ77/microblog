from fastapi import APIRouter

from backend.api.logger import LoggingRoute


router = APIRouter(
    route_class=LoggingRoute,
    prefix='/hello',
    tags=['Hello']
)


@router.get('/')
async def get_hello():
    return {'msg': 'Hello world!'}
