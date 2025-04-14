from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    password: str
    email: EmailStr


class UserUpdate(BaseModel):
    name: Optional[str]
    password: Optional[str]
    email: Optional[EmailStr]


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
