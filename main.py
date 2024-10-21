import datetime

import sqlalchemy
from sqlalchemy import create_engine, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, ForeignKey, Date, Time

from Users import User
from Positions import Position
from Rooms import Room
from Reserves import Reserve


# --- Define the Base for Models ---
Base = sqlalchemy.orm.declarative_base();

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
    database_url = 'mysql+mysqlconnector://root:1234@localhost:3306/projectDataBase2'
    session = get_session(database_url)

    # User.addUser(session,"Borbath Matyas", "borbath.matyas@student.ms.sapientia.ro", 100, 3)
    User.addUser(session,"Korpos Botond", "korpos.botond@student.ms.sapientia.ro", 100, 3)



