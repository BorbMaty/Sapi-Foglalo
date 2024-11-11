# app/schemas/reserve.py
from pydantic import BaseModel
from typing import Optional

class ReserveCreate(BaseModel):
    UserId: int
    RoomId: int
    Date: str  # 'YYYY-MM-DD' format
    StartHour: str  # 'HH:MM' format
    EndHour: str  # 'HH:MM' format

class ReserveResponse(BaseModel):
    ReserveId: int
    UserId: int
    RoomId: int
    Date: str
    StartHour: str
    EndHour: str

    class Config:
        orm_mode = True
