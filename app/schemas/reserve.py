# app/schemas/reserve.py
from pydantic import BaseModel
from datetime import date, time

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class RoomResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True

class ReserveCreate(BaseModel):
    user_id: int
    room_id: int
    date: date
    start_hour: time
    end_hour: time

class ReserveResponse(BaseModel):
    ReserveId: int
    UserId: int
    RoomId: int
    Date: date
    StartHour: time
    EndHour: time
    user: UserResponse  # Nested User
    room: RoomResponse  # Nested Room

    class Config:
        from_attributes = True

class MinimalReserveResponse(BaseModel):
    room: int
    date: date
    start_time: time
    end_time: time
