import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Importing models
from models import User, Room, Position

# Importing routes
from routes import Reserves, fast

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
    database_url = 'mysql+pymysql://root:Almafa%401@localhost/RoomReserver'
    session: Session = get_session(database_url)
    User.addUser(session,"Borbath Matyas", "borbath.matyas@student.ms.sapientia.ro", 100, 3)
    #User.addUser(session, "Korpos Botond", "korpos.botond@student.ms.sapientia.ro", 100, 3)
    Room.addRoom(session,230)