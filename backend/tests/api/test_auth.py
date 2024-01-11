import random
import hashlib
import string


def signup_user(client):
    body = {
        "username": "Greg",
        "login": ''.join(random.choice(
            string.ascii_letters + string.digits) for _ in range(100)),
        "password": "fake_password",
        "avatar": "http://microblog.com/avatars/Greg.png"
    }
    response = client.post("/auth/signup", json=body).json()

    data = {
        "id": response["id"],
        "token": response["token"],
        "login": body["login"],
        "password": body["password"]
    }

    return data


def test_signup(client):
    body = {
        "username": "Greg",
        "login": ''.join(random.choice(
            string.ascii_letters + string.digits) for _ in range(100)),
        "password": hashlib.sha256("fake_password".encode()).hexdigest(),
        "avatar": "http://microblog.com/avatars/Greg.png"
    }

    response = client.post("/auth/signup", json=body)
    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'token' in response.json()
    assert 'token' in response.cookies

    # second signup fails because of the same login
    response = client.post("/auth/signup", json=body)
    assert response.status_code == 400


def test_login(client):
    new_user = signup_user(client)
    body = {
        "login": new_user["login"],
        "password": new_user["password"]
    }
    response = client.post("/auth/login", json=body)
    assert response.status_code == 200
    assert 'token' in response.json()
    assert 'token' in response.cookies


def test_login_fails(client):
    body = {
        "login": "login that completely doesn't exist",
        "password": "fake password"
    }
    response = client.post("/auth/login", json=body)
    assert response.status_code == 401

    response = client.post("/auth/login", json={})
    assert response.status_code == 400


def test_logout(client):
    new_user = signup_user(client)
    token = new_user["token"]
    response = client.post("/auth/logout", cookies={"token": token})
    assert response.status_code == 200
    assert 'token' in response.cookies
