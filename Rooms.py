import sqlalchemy
from sqlalchemy import Integer, Column

Base = sqlalchemy.orm.declarative_base()

class Room(Base):
    __tablename__ = 'Room'

    id = Column(Integer, primary_key=True)

    def __init__(self, id):
        self.id = id

    def addRoom(session,id):
        new_room = Room(id)
        session.add(new_room)
        session.commit()
