import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Importing models
from models import User, Room, Position

from models.Rooms import Room, RoomDAL

# Importing routes
from routes import Reserves, fast
from routes.Reserves import ReserveDAL

# --- Define the Base for Models ---
Base = sqlalchemy.orm.declarative_base()

def get_session(db_url):
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    return Session()


# --- Create Database Function ---
def create_database(db_url):
    # Create the engine (connects to the database)
    engine = create_engine(db_url)

    # Create the tables in the database
    Base.metadata.create_all(engine)

    print("Database and User table created successfully!")


if __name__ == "__main__":
    database_url = 'mysql+mysqlconnector://root:1234@localhost:3306/testDB'

    session: Session = get_session(database_url)
    # create_database(database_url)

    # TODO: move DAL initialization to a separate function
    reserve_dal = ReserveDAL(session)

    # TODO: refactor this to DAL version
    # User.addUser(session,"Borbath Matyas", "borbath.matyas@student.ms.sapientia.ro", 100, 3)

    room_dal = RoomDAL(session=session)

    # This is working
    # result = room_dal.addRoom(room_id=314)

    # User.addUser(session, "Korpos Botond", "korpos.botond@student.ms.sapientia.ro", 100, 3)
    # User.deleteUserByID(session,9)

    # result = reserve_dal.addReserve(user_id=1,
    #                                 room_id=313,
    #                                 date='2024-10-30',
    #                                 start_hour='09:00:00',
    #                                 end_hour='10:00:00')

    result = reserve_dal.getAllReserves()
    print(result)


# Create python venv 
# python -m venv .venv

# Activate venv 
# On Windows
# cmd.exe
# C:\> <venv>\Scripts\activate.bat
# PowerShell
# PS C:\> <venv>\Scripts\Activate.ps1

# Install all requirements 
# pip install -r requirements.txt