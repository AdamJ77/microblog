import random
import hashlib
import string


def test_signup(client):
    body = {
        "username": "Greg",
        "login": ''.join(random.choice(
            string.ascii_letters + string.digits) for _ in range(10)),
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
