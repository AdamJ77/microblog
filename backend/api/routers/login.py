from fastapi import APIRouter, Request, HTTPException, Depends
# from starlette.requests import Request

from backend.api.logger import LoggingRoute
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

users = [
    {
        "id": "d19ffe4b-d2e1-43d9-8679-c8a21309ac22",
        "login": "login1",
        "password": "pass1",
        "name": "Elon Musk"
    },
    {
        "id": "048358e2-42bf-4c1b-9569-7301902c11c7",
        "login": "login2",
        "password": "pass2",
        "name": "Suchoklates"
    },
]

SECRET_KEY = "your-secret-key"

# Algorithm to use for JWT
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Function to create a JWT token
def create_jwt_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


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

    found_user = None
    for user in users:
        if login == user["login"] and password == user["password"]:
            found_user = user
            break
    
    if not found_user:
        raise HTTPException(status_code=401)

    token_data = { "id": found_user["id"] }
    access_token = create_jwt_token(token_data)

    return {"token": access_token}


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
    except JWTError:
        raise credentials_exception
    return id


@router.get("/test")
async def login_test(user_id: str = Depends(get_current_user)):
    found_name = None
    for user in users:
        if user["id"] == user_id:
            found_name = user["name"]
            break
        
    return {"name": found_name}
