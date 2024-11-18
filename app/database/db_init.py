from app.database.database import engine, Base, Session
from app.models.position import PositionDAL
from app.models.position import Position
from app.models.user import UserDAL
from app.models.user import User
from app.models.room import RoomDAL
from app.models.room import Room
from app.models.reserve import ReserveDAL
from app.models.reserve import Reserve
from datetime import date, time, datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from .endpoints import router  # Import your endpoints router

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)


# Create database tables
Base.metadata.create_all(bind=engine)


def main():
    db_session = Session()
    try:
        position_dal = PositionDAL(db_session)
        room_dal = RoomDAL(db_session)
        user_dal = UserDAL(db_session)
        reserves_dal = ReserveDAL(db_session)

        # new_reservation = reserves_dal.create_reserve(
        #     1,
        #     114,
        #     datetime.strptime("2024.11.12", "%Y.%m.%d").date(),
        #     datetime.strptime("9.00", "%H.%M").time(),
        #     datetime.strptime("11.00", "%H.%M").time()
        # )
        #
        new_reservation = reserves_dal.create_reserve(
            2,
            114,
            datetime.strptime("2024.11.12", "%Y.%m.%d").date(),
            datetime.strptime("11.00", "%H.%M").time(),
            datetime.strptime("12.00", "%H.%M").time()
        )

        # for i in range(12, 20):
        #     reserves_dal.delete_reserve_by_id(i)

    except Exception as e:
        db_session.rollback()  # Rollback in case of an error
        print(f"An error occurred: {e}")

    finally:
        db_session.close()  # Ensure the session is closed


if __name__ == "__main__":
    main()
