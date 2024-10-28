import sqlalchemy
from sqlalchemy import Integer, Column
from sqlalchemy.orm import relationship

Base = sqlalchemy.orm.declarative_base()

class Room(Base):
    __tablename__ = 'Rooms'

    id = Column(Integer, primary_key=True)

    reservations = relationship('Reserves', backref='Room') 

    def __init__(self, id):
        self.id = id


class RoomDAL:
    def __init__(self, session):
        self.session = session

    def addRoom(self, room_id : int):
        new_room = Room(room_id)
        self.session.add(new_room)
        self.session.commit()
        return new_room

    def getRoom(self, room_id):
        return self.session.query(Room).filter(Room.id == room_id).first()

    def getAllRooms(self):
        return self.session.query(Room).all()

    def updateRoom(self, room_id, new_room_id):
        room = self.get_room(room_id)
        if room:
            room.id = new_room_id
            self.session.commit()
        return room

    def deleteRoom(self, room_id):
        room = self.get_room(room_id)
        if room:
            self.session.delete(room)
            self.session.commit()
        return room

# Example usage
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('your_database_url')
# Session = sessionmaker(bind=engine)
# session = Session()

# dal = RoomDAL(session)
# dal.add_room(1)
# room = dal.get_room(1)
# print(room)
# all_rooms = dal.get_all_rooms()
# print(all_rooms)
# dal.update_room(1, 2)
# dal.delete_room(2)
# session.close()
