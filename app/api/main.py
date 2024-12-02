from fastapi import FastAPI, HTTPException, Depends
from app.api.users_router import users_router
from app.api.rooms_router import rooms_router
from app.api.reserves_router import reserves_router
from app.api.positions_router import positions_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.reserve import Reserve  # Import your Reserve model
from app.schemas.reserve import ReserveCreate, ReserveResponse  # Use appropriate Pydantic schemas

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend's development URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers with their respective prefixes and tags
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(rooms_router, prefix="/rooms", tags=["Rooms"])
app.include_router(reserves_router, prefix="/reserves", tags=["Reserves"])
app.include_router(positions_router, prefix="/positions", tags=["Positions"])

# Use the absolute path to the static directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/images", StaticFiles(directory="app/images"), name="images")

# API Endpoints
@app.get("/api/message")
async def get_message():
    return {"message": "Hello from FastAPI!"}


@app.post("/api/book-room", response_model=ReserveResponse)
async def book_room(reserve: ReserveCreate, db: Session = Depends(get_db)):
    # Check for conflicting reservations
    existing_reservations = db.query(Reserve).filter(
        Reserve.room_id == reserve.room_id,
        Reserve.date == reserve.date,
        Reserve.start_hour < reserve.end_hour,
        Reserve.end_hour > reserve.start_hour
    ).all()

    if existing_reservations:
        raise HTTPException(
            status_code=400,
            detail="This time slot is already reserved."
        )

    # Create the new reservation
    new_reserve = Reserve(
        user_id=reserve.user_id,
        room_id=reserve.room_id,
        date=reserve.date,
        start_hour=reserve.start_hour,
        end_hour=reserve.end_hour,
    )
    db.add(new_reserve)
    db.commit()
    db.refresh(new_reserve)

    return new_reserve


@app.get("/api/bookings", response_model=list[ReserveResponse])
async def get_bookings(db: Session = Depends(get_db)):
    # Fetch all reservations
    reservations = db.query(Reserve).all()
    return reservations


# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello from the API"}

#todo I need to fix issues with the Reserve Logic