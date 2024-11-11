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
        position_dal = PositionDAL(db_session)
        room_dal = RoomDAL(db_session)
        user_dal = UserDAL(db_session)
        reserves_dal = ReserveDAL(db_session)


        # new_position = position_dal.create_position(position_id=1,name="Szamtech")
        # new_position = position_dal.create_position(name="Auto")

        # x = position_dal.get_all_positions()
        # print(x)

        # position_dal.get_all_positions()
        # room_dal.get_all_rooms()
        room_dal.get_room_by_id(115)

        # Create a new RoomDAL instance and add a room
        # new_room = room_dal.create_room(114)

        # Create a user
        # new_user = user_dal.create_user("matyi", "matyi@gmail.com",1,3)

        # id = user_dal.get_id_by_name("matyi")
        # print(id)

        # new_reserve = reserves_dal.create_reserve(1, 114, "2024.11.05", 9, 11)
        # #position_dal.delete_position(101)
     
    except Exception as e:
        db_session.rollback()  # Rollback in case of an error
        print(f"An error occurred: {e}")
        
    finally:
        db_session.close()  # Ensure the session is closed

if __name__ == "__main__":
    main()
