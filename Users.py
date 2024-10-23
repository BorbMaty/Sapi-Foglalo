import sqlalchemy
from sqlalchemy import Integer, Column
from sqlalchemy import create_engine, String

Base = sqlalchemy.orm.declarative_base()

class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    position = Column(String, nullable=False)
    year = Column(Integer, nullable=True)

    def __init__(self, name, email, position, year=None):
        self.name = name
        self.email = email
        self.position = position
        self.year = year

    def addUser(session, name, email, position, year=None):
        # Új felhasználó hozzáadása az adatbázishoz.
        new_user = Users(name=name, email=email, position=position, year=year)
        session.add(new_user)
        session.commit()
