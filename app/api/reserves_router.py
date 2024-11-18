# app/api/reserves_router.py
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.reserve import ReserveCreate, ReserveResponse
from app.models.reserve import ReserveDAL
from app.database import get_db

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
