import sqlalchemy
from sqlalchemy import Integer, Column, ForeignKey, Date, Time
from sqlalchemy.orm import relationship

import Users
from Users import User
from Rooms import Room

Base = sqlalchemy.orm.declarative_base()

class Reserve(Base):
    __tablename__ = 'Reserves'

    ReserveId = Column(Integer, primary_key=True, autoincrement=True)
    UserId = Column(Integer, ForeignKey('Users.id'), nullable=False)
    RoomId = Column(Integer, ForeignKey('Room.id'), nullable=False)
    Date = Column(Date, nullable=False)
    StartHour = Column(Time, nullable=False)
    EndHour = Column(Time, nullable=False)

    user = relationship("User", backref="reserves")
    room = relationship("Room", backref="reserves")

    def __init__(self, UserId, RoomId, Date, StartHour, EndHour):
        self.UserId = UserId
        self.RoomId = RoomId
        self.Date = Date
        self.StartHour = StartHour
        self.EndHour = EndHour

def addReserve(session, user_id, room_id, date, start_hour, end_hour):
    new_reserve = Reserve(UserId=user_id, RoomId=room_id, Date=date, StartHour=start_hour, EndHour=end_hour)
    session.add(new_reserve)
    session.commit()
    return new_reserve