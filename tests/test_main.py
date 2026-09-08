from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# TC01: รหัสผ่านถูก
def test_login_correct_password():
    response = client.post(
        "/login",
        json={
            "username": "admin",
            "password": "1234"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"


# TC02: รหัสผ่านผิด
def test_login_wrong_password():
    response = client.post(
        "/login",
        json={
            "username": "admin",
            "password": "wrong"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password"


# TC03: ไม่มีผู้ใช้
def test_login_user_not_found():
    response = client.post(
        "/login",
        json={
            "username": "unknown",
            "password": "1234"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password"
```
