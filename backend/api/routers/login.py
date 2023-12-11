from fastapi import APIRouter, Request, HTTPException
# from starlette.requests import Request

from backend.api.logger import LoggingRoute

router = APIRouter(
    route_class=LoggingRoute,
    prefix='/login',
    tags=['Login']
)

@router.post("/")
async def login(request: Request):
    data = await request.form()

    login = data.get("login")
    password = data.get("password")

    if not login or not password:
        raise HTTPException(status_code=400, detail="Login and password are required")

    if login != "login" or password != "pass":
        raise HTTPException(status_code=401)

    return {"message": "Login successful"}