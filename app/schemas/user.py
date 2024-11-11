# schemas/user.py
from pydantic import BaseModel
from typing import Optional

class PositionResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    name: str
    email: str
    PositionId: int
    year: Optional[int] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    Position: PositionResponse  # Nested PositionResponse schema
    year: Optional[int] = None

    class Config:
        orm_mode = True
