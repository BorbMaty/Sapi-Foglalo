import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import Reserves
from Positions import Position
from Users import User
from Rooms import Room
from Reserves import Reserve


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
    #database_url = 'mysql+pymysql://borbmaty:Almafa2@192.168.172.207:3306/ProjectDatabase'
    # database_url = 'mysql+pymysql://boti:boti@192.168.172.207:3306/ProjectDatabase'
    #database_url = 'mysql+pymysql://jeno:jeno@192.168.172.207:3306/ProjectDatabase'

    database_url = 'mysql+mysqlconnector://root:1234@localhost:3306/testDB'

    session = get_session(database_url)

    # User.addUser(session, "Korpos Botond2", "korpos.botond@student.ms.sapientia.ro", 100, 3)
    User.deleteUserByID(session, 7)