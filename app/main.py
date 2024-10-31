from app.database import engine, Base, Session
from app.models.position import PositionDAL
from app.models.position import Position
from app.models.user import UserDAL
from app.models.user import User
from app.models.room import RoomDAL
from app.models.room import Room
from app.models.reserve import ReserveDAL
from app.models.reserve import Reserve
from datetime import date,time

# Create database tables
Base.metadata.create_all(bind=engine)

def main():
    db_session = Session()
    try:
        # Create a new PositionDAL instance and add a position
        position_dal = PositionDAL(db_session)
        # Uncomment the line below to add a position
        new_position = position_dal.create_position(name="Automat")
        
        # Create a new RoomDAL instance and add a room
        room_dal = RoomDAL(db_session)
        #new_room = room_dal.create_room(230)
        user_dal = UserDAL(db_session)
        #new_user = user_dal.create_user("Borbáth Mátyás-Levente", "borbath.matyas@student.ms.sapientia.ro",100,3)
        reserve_dal = ReserveDAL(db_session)
        user_id = 1
        room_id = 230
        reserve_date = date(2024, 10, 31)
        start_hour = time(9, 0)  # 9:00 AM
        end_hour = time(11, 0)   # 11:00 AM
        #new_reserve = reserve_dal.create_reserve(user_id, room_id, reserve_date, start_hour, end_hour)
        #position_dal.delete_position(101)
     
    except Exception as e:
        db_session.rollback()  # Rollback in case of an error
        print(f"An error occurred: {e}")
        
    finally:
        db_session.close()  # Ensure the session is closed

if __name__ == "__main__":
    main()
