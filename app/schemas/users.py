from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    password: str
    email: str


class UserUpdate(BaseModel):
    name: Optional[str]
    password: Optional[str]
    email: Optional[str]


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
