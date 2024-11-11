# app/api/positions_router.py
from fastapi import APIRouter, Depends
from app.schemas import PositionCreate, PositionResponse  # Import schemas for validation and response
from app.models.position import PositionDAL  # Import the DAL for positions
from app.database import get_db  # Dependency for database session
from sqlalchemy.orm import Session

positions_router = APIRouter()

@positions_router.get("/")
async def get_users():
    return {"message": "Positions endpoint"}

# Dependency to get the PositionDAL instance
def get_position_dal(db: Session = Depends(get_db)):
    return PositionDAL(db)

@positions_router.post("/", response_model=PositionResponse)
def create_position(position: PositionCreate, position_dal: PositionDAL = Depends(get_position_dal)):
    return position_dal.create_position(
        name=position.name
    )
