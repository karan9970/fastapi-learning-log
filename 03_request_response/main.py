from fastapi import FastAPI, HTTPException
from typing import List
from schemas import UserCreate, UserUpdate, UserResponse

app = FastAPI()

# fake DB
user_db = []
counter = 1


@app.get("/")
def home():
    return {"msg": "Day 3: Request and Response Models"}


# CREATE user
@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    global counter

    new_user = {
        "id": counter,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "is_active": True
    }

    user_db.append(new_user)
    counter += 1
    return new_user


# GET all users
@app.get("/users", response_model=List[UserResponse])
def get_all_users():
    return user_db


# UPDATE user
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    for db_user in user_db:
        if db_user["id"] == user_id:
            if user.name is not None:
                db_user["name"] = user.name
            if user.age is not None:
                db_user["age"] = user.age
            return db_user

    raise HTTPException(status_code=404, detail="User not found")
