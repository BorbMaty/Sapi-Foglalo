# app/api/positions_router.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import PositionCreate, PositionResponse
from app.models.position import Position
from app.database import get_db

positions_router = APIRouter()

@positions_router.get("/", response_model=list[PositionResponse])
async def get_positions(db: Session = Depends(get_db)):
    """Retrieve all positions."""
    positions = db.query(Position).all()
    return positions

@positions_router.get("/{position_id}", response_model=PositionResponse)
async def get_position(position_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific position by ID."""
    position = db.query(Position).filter(Position.id == position_id).first()
    if not position:
        raise HTTPException(status_code=404, detail="Position not found")
    return position

@positions_router.post("/", response_model=PositionResponse)
async def create_position(position: PositionCreate, db: Session = Depends(get_db)):
    """Create a new position."""
    existing_position = db.query(Position).filter(Position.name == position.name).first()
    if existing_position:
        raise HTTPException(status_code=400, detail="Position already exists")
    
    db_position = Position(name=position.name)
    db.add(db_position)
    db.commit()
    db.refresh(db_position)
    return db_position

@positions_router.put("/{position_id}", response_model=PositionResponse)
async def update_position(position_id: int, position: PositionCreate, db: Session = Depends(get_db)):
    """Update an existing position."""
    db_position = db.query(Position).filter(Position.id == position_id).first()
    if not db_position:
        raise HTTPException(status_code=404, detail="Position not found")

    db_position.name = position.name
    db.commit()
    db.refresh(db_position)
    return db_position

@positions_router.delete("/{position_id}", status_code=204)
async def delete_position(position_id: int, db: Session = Depends(get_db)):
    """Delete a position by ID."""
    position = db.query(Position).filter(Position.id == position_id).first()
    if not position:
        raise HTTPException(status_code=404, detail="Position not found")
    db.delete(position)
    db.commit()
    return {"detail": "Position deleted successfully"}
