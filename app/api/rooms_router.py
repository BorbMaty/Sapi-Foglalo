# app/api/rooms_router.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import RoomCreate, RoomResponse
from app.models.room import Room
from app.database import get_db

rooms_router = APIRouter()

@rooms_router.get("/", response_model=list[RoomResponse])
async def get_rooms(db: Session = Depends(get_db)):
    """Retrieve all rooms."""
    rooms = db.query(Room).all()
    return rooms

@rooms_router.get("/{room_id}", response_model=RoomResponse)
async def get_room(room_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific room by ID."""
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@rooms_router.post("/", response_model=RoomResponse)
async def create_room(room: RoomCreate, db: Session = Depends(get_db)):
    """Create a new room with the given ID."""
    existing_room = db.query(Room).filter(Room.id == room.id).first()
    if existing_room:
        raise HTTPException(status_code=400, detail="Room already exists")
    db_room = Room(id=room.id)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

@rooms_router.put("/{room_id}", response_model=RoomResponse)
async def update_room(room_id: int, room: RoomCreate, db: Session = Depends(get_db)):
    """Update an existing room's ID."""
    db_room = db.query(Room).filter(Room.id == room_id).first()
    if not db_room:
        raise HTTPException(status_code=404, detail="Room not found")
    
    # Assuming you want to update the room's ID
    db_room.id = room.id
    db.commit()
    db.refresh(db_room)
    return db_room

@rooms_router.delete("/{room_id}", status_code=204)
async def delete_room(room_id: int, db: Session = Depends(get_db)):
    """Delete a room by its ID."""
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    db.delete(room)
    db.commit()
    return {"detail": "Room deleted successfully"}
