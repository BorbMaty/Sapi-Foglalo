import datetime

import sqlalchemy
from sqlalchemy import create_engine, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, ForeignKey, Date, Time

# --- Define the Base for Models ---
Base = sqlalchemy.orm.declarative_base();

def get_session(db_url):
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    return Session()




# --- Define the User model ---
class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    position = Column(String, nullable=False)
    year = Column(Integer, nullable=True)


class Position(Base):
    __tablename__ = 'Position'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Room(Base):
    __tablename__ = 'Room'

    id = Column(Integer, primary_key=True)


class Reserve(Base):
    __tablename__ = 'Reserve'

    ReserveId = Column(Integer, primary_key=True)
    UserId = Column(Integer, ForeignKey('User.id'), nullable=False)
    RoomId = Column(Integer, ForeignKey('Room.id'), nullable=False)
    Date = Column(Date, nullable=False)
    StartHour = Column(Time, nullable=False)
    EndHour = Column(Time, nullable=False)


# --- Create Database Function ---
def create_database(db_url):
    # Create the engine (connects to the database)
    engine = create_engine(db_url)

    # Create the tables in the database
    Base.metadata.create_all(engine)

    print("Database and User table created successfully!")


# Call the function to create the database (e.g., SQLite)
if __name__ == "__main__":
    # Replace this with your desired database URL
    database_url = 'mysql+mysqlconnector://root:1234@localhost:3306/projectDataBase2'  # SQLite database in current directory
    session = get_session(database_url)

    new_user = User(name='John Doe', email='john.doe@example.com', position='Manager', year=1)
    session.add(new_user)
    session.commit()
    # create_database(database_url)


