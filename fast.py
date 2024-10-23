from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import json

app = FastAPI()

# Serve static files (like your HTML file)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define the booking data model
class Booking(BaseModel):
    room_id: str
    user_id: str
    date: str
    start_hour: str
    end_hour: str

# Variable to store reservations
reservations = []

# Root endpoint to serve HTML file
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/booking.html") as f:
        return f.read()

# Booking endpoint to handle reservations
@app.post("/reserve")
async def reserve_room(booking: Booking):
    # Create a reservation entry
    reservation_entry = {
        "room_id": booking.room_id,
        "user_id": booking.user_id,
        "date": booking.date,
        "start_hour": booking.start_hour,
        "end_hour": booking.end_hour,
    }
    # Store the reservation
    reservations.append(reservation_entry)
    return {"message": f"Room {booking.room_id} booked by user {booking.user_id} on {booking.date} from {booking.start_hour} to {booking.end_hour}."}

@app.get("/reservations")
async def get_reservations():
    return {"reservations": reservations}