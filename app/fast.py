from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import json

import firebase_admin
from  firebase_admin import db, credentials

from datetime import datetime


app = FastAPI()

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred,{"databaseURL": "https://teremfoglalas-faa5b-default-rtdb.europe-west1.firebasedatabase.app/"})

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
reserve_ref = db.reference("/Reserves")

def check_date_collision(date, start_hour, end_hour):
    # Convert string dates to datetime objects
    start_hour = datetime.strptime(start_hour, "%H:%M")
    end_hour = datetime.strptime(end_hour, "%H:%M")
    date = datetime.strptime(date,"%Y-%m-%d")

    # Fetch existing date ranges from Firestore
    date_ranges_ref = db.reference('/Reservations')
    existing_data_ranges = date_ranges_ref.get()

    print(existing_data_ranges)

    for existing_data in existing_data_ranges.values():
        existing_start = datetime.strptime(existing_data['start_hour'], "%H:%M")
        existing_end = datetime.strptime(existing_data['end_hour'], "%H:%M")
        existing_date = datetime.strptime(existing_data['date'], "%Y-%m-%d")

        # Check for overlap
        if (start_hour <= existing_end) and (end_hour >= existing_start) and (date == existing_date):
            return True  # Collision detected

    return False  # No collision

# Root endpoint to serve HTML file
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/booking2.html") as f:

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

    if check_date_collision(booking.date, booking.start_hour, booking.end_hour):
        raise HTTPException(status_code=400, detail="Room is already reserved for the selected time.")
    else:
        reserve_ref.push(reservation_entry)

    # Store the reservation
    return {"message": f"Room {booking.room_id} booked by user {booking.user_id} on {booking.date} from {booking.start_hour} to {booking.end_hour}."}

@app.get("/reserves")
async def get_reservations():
    return {"reserves": reservations}

