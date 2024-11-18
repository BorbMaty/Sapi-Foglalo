# app/api/main.py
from fastapi import FastAPI
from app.api.users_router import users_router  # Correctly import 'users_router'
from app.api.rooms_router import rooms_router
from app.api.reserves_router import reserves_router
from app.api.positions_router import positions_router
from fastapi.middleware.cors import CORSMiddleware

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

# Root route to test the connection
@app.get("/")
async def read_root():
    return {"message": "Welcome to the API!"}
