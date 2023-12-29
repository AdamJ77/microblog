from fastapi import APIRouter, Request, HTTPException, Depends

from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import secrets
import hashlib

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET", None)
if not SECRET_KEY:
    print("No secret key given. Generating random...")
    SECRET_KEY = secrets.token_hex(16)

ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

ip_token_storage = {}


def create_jwt_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=7)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("id")
        if id is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception
    return id


router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@router.post("/login")
async def login(request: Request):
    data = await request.json()

    login = data.get("login")
    password = data.get("password")

    if not login or not password:
        raise HTTPException(status_code=400,
                            detail="Login and password are required")

    db = request.app.database

    user = await db.users.find_one({
        "login": login,
        "password": hashlib.sha256(password.encode()).hexdigest()
    })

    if not user:
        raise HTTPException(status_code=401,
                            detail="Invalid login or password")

    token_data = {
        "id": str(user["_id"])
    }
    access_token = create_jwt_token(token_data)

    ip_address = request.client.host
    ip_token_storage[ip_address] = access_token

    response = JSONResponse(content={"token": access_token})

    return response


@router.post("/refresh")
async def refresh(
    request: Request,
    response: JSONResponse,
    user_id: str = Depends(get_current_user)
):
    token_data = {
        "id": user_id
    }
    access_token = create_jwt_token(token_data)

    ip_address = request.client.host
    try:
        ip_token_storage[ip_address] = access_token
    except KeyError:
        raise HTTPException(status_code=401, detail="No saved token.")

    response = JSONResponse(content={"token": access_token})

    return response


@router.get("/init")
async def init(request: Request):
    ip_address = request.client.host
    try:
        access_token = ip_token_storage[ip_address]
    except KeyError:
        raise HTTPException(status_code=401, detail="No saved token.")

    response = JSONResponse(content={"token": access_token})

    return response


@router.post("/logout")
async def logout(request: Request, user_id: str = Depends(get_current_user)):
    ip_address = request.client.host
    try:
        del ip_token_storage[ip_address]
    except KeyError:
        raise HTTPException(status_code=401, detail="No saved token.")

    response = JSONResponse(content={"message": "Logged out successfully."})

    return response


@router.post("/signup")
async def signup(request: Request):
    data = await request.json()

    username = data.get("username")
    login = data.get("login")
    password = data.get("password")
    avatar = data.get("avatar")

    db = request.app.database

    if await db.users.find_one({"login": login}):
        raise HTTPException(status_code=400,
                            detail="User with given login exists.")

    result = await db.users.insert_one({
        "login": login,
        "password": hashlib.sha256(password.encode()).hexdigest(),
        "avatar": avatar,
        "username": username
    })

    user_id = str(result.inserted_id)
    return {"id": user_id}
