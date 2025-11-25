from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    is_active: bool = True


class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
