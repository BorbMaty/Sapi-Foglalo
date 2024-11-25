# app/api/reserves_router.py
from datetime import date
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.reserve import ReserveCreate, ReserveResponse
from app.models.reserve import Reserve, ReserveDAL
from app.database import get_db
from app.models.query_dal import QueryDAL
from app.database.database import Session

reserves_router = APIRouter()

def get_reserve_dal(db=Depends(get_db)):
    return ReserveDAL(db)

@reserves_router.get("/", response_model=list[ReserveResponse])
async def get_reserves(reserve_dal: ReserveDAL = Depends(get_reserve_dal)):
    reserves = reserve_dal.get_all_reserves()
    return [ReserveResponse.from_orm(reserve) for reserve in reserves]

@reserves_router.get("/{reserve_id}", response_model=ReserveResponse)
async def get_reserve(reserve_id: int, reserve_dal: ReserveDAL = Depends(get_reserve_dal)):
    reserve = reserve_dal.get_reserve_by_id(reserve_id)
    if not reserve:
        raise HTTPException(status_code=404, detail="Reserve not found")
    return ReserveResponse.from_orm(reserve)

@reserves_router.post("/", response_model=ReserveResponse)
async def create_reserve(reserve: ReserveCreate, reserve_dal: ReserveDAL = Depends(get_reserve_dal)):
    new_reserve = reserve_dal.create_reserve(
        user_id=reserve.user_id,
        room_id=reserve.room_id,
        reserve_date=reserve.date,
        start_hour=reserve.start_hour,
        end_hour=reserve.end_hour
    )
    return ReserveResponse.from_orm(new_reserve)

@reserves_router.post("/api/book-room", response_model=ReserveResponse)
async def book_room(reserve: ReserveCreate, reserve_dal: ReserveDAL = Depends(get_reserve_dal)):
    # Check if the room is already reserved for the given time
    existing_reservation = reserve_dal.get_conflicting_reserve(
        room_id=reserve.room_id,
        reserve_date=reserve.date,
        start_hour=reserve.start_hour,
        end_hour=reserve.end_hour
    )
    if existing_reservation:
        raise HTTPException(status_code=400, detail="Room is already reserved for the specified time.")

    # Create the new reservation
    new_reserve = reserve_dal.create_reserve(
        user_id=reserve.user_id,
        room_id=reserve.room_id,
        reserve_date=reserve.date,
        start_hour=reserve.start_hour,
        end_hour=reserve.end_hour
    )
    return ReserveResponse.from_orm(new_reserve)

@reserves_router.put("/{reserve_id}", response_model=ReserveResponse)
async def update_reserve(reserve_id: int, reserve_data: ReserveCreate, reserve_dal: ReserveDAL = Depends(get_reserve_dal)):
    updated = reserve_dal.update_reserve(
        reserve_id=reserve_id,
        start_hour=reserve_data.start_hour,
        end_hour=reserve_data.end_hour
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Reserve not found")
    reserve = reserve_dal.get_reserve_by_id(reserve_id)
    return ReserveResponse.from_orm(reserve)

@reserves_router.delete("/{reserve_id}", status_code=204)
async def delete_reserve(reserve_id: int, reserve_dal: ReserveDAL = Depends(get_reserve_dal)):
    reserve_deleted = reserve_dal.delete_reserve(reserve_id)
    if not reserve_deleted:
        raise HTTPException(status_code=404, detail="Reserve not found")
    return {"detail": "Reserve deleted successfully"}


router = APIRouter(prefix="/reserves", tags=["Reserves"])

@reserves_router.get("/reservations/{room_id}/{reservation_date}", response_model=list[ReserveResponse])
def get_reservations_for_room(
    room_id: int,
    reservation_date: date,
    db: Session = Depends(get_db)
):
    """
    Fetch all reservations for a specific room on a given date.

    Args:
        room_id (int): The ID of the room.
        reservation_date (date): The date for which reservations are requested.

    Returns:
        List of reservations for the room on the given date.
    """
    reservations = db.query(Reserve).filter(
        Reserve.RoomId == room_id,
        Reserve.Date == reservation_date
    ).all()

    if not reservations:
        raise HTTPException(status_code=404, detail="No reservations found for the specified room and date.")

    return reservations
