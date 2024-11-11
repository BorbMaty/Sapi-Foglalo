from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Room  # Adjust based on your model definitions
from .schemas import RoomSchema  # Pydantic schema for Room

router = APIRouter()

@router.get("/rooms", response_model=list[RoomSchema])
def get_rooms(db: Session = Depends(get_db)):
    rooms = db.query(Room).all()
    return rooms

# Define more endpoints here as needed
