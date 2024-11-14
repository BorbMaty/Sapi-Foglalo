# app/schemas.py
from pydantic import BaseModel

class RoomCreate(BaseModel):
    id: int

class RoomResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True  # This ensures compatibility with the Room model
