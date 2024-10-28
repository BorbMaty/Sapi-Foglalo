import sqlalchemy
from sqlalchemy import Integer, Column, ForeignKey, Date, Time
from sqlalchemy.orm import relationship

Base = sqlalchemy.orm.declarative_base()

class Reserve(Base):
    __tablename__ = 'Reserve'

    ReserveId = Column(Integer, primary_key=True, autoincrement=True)
    UserId = Column(Integer, ForeignKey('User.id'), nullable=False)
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

    def addReserve(session, UserId, RoomId, Date, StartHour, EndHour):
        new_reserve = Reserve(UserId=UserId, RoomId=RoomId, Date=Date, StartHour=StartHour, EndHour=EndHour)
        session.add(new_reserve)
        session.commit()
