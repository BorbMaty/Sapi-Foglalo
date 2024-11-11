# app/api/reserves_router.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db  # Assuming this is defined in app/database.py
from app.models.reserve import ReserveDAL  # Import the DAL class for reserves
from app.schemas import ReserveCreate, ReserveResponse  # Import schemas for validation and responses

reserves_router = APIRouter()

@reserves_router.get("/")
async def get_users():
    return {"message": "Reserves endpoint"}


# Dependency to get the ReserveDAL instance
def get_reserve_dal(db: Session = Depends(get_db)):
    return ReserveDAL(db)

@reserves_router.post("/", response_model=ReserveResponse)
def create_reservation(reservation: ReserveCreate, reserve_dal: ReserveDAL = Depends(get_reserve_dal)):
    # Create a new reservation using ReserveDAL
    return reserve_dal.create_reserve(
        UserId=reservation.UserId,
        RoomId=reservation.RoomId,
        Date=reservation.Date,
        StartHour=reservation.StartHour,
        EndHour=reservation.EndHour
    )
