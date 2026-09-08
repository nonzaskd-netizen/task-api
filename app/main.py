from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(data: LoginRequest):

    if data.username == "admin123" and data.password == "1234":
        return {
            "message": "Login successful"
        }

    raise HTTPException(
        status_code=401,
        detail="Invalid username or password"
    )