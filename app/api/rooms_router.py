# app/api/rooms_router.py
from fastapi import APIRouter
from app.schemas import RoomCreate, RoomResponse  # Ensure this import is correct

rooms_router = APIRouter()

@rooms_router.get("/")
async def get_users():
    return {"message": "Rooms endpoint"}


@rooms_router .post("/", response_model=RoomResponse)
def create_room(room: RoomCreate):
    # Your room creation logic here
    return room
