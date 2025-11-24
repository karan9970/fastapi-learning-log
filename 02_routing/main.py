from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This is just fake DB (list)
users = []


class User(BaseModel):
    id: int
    name: str
    age: int


# Basic GET
@app.get("/")
def home():
    return {"message": "Day 2: Routing & Methods"}


# GET with PATH parameter
@app.get("/user/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}


# GET with QUERY parameter
@app.get("/search")
def search_user(name: str):
    for user in users:
        if user["name"].lower() == name.lower():
            return user
    return {"error": "User not found"}


# POST (add new user)
@app.post("/create")
def create_user(user: User):
    users.append(user.dict())
    return {"message": "User added", "user": user}
