import sqlalchemy
from sqlalchemy import Integer, Column, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from Users import Users
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

    user = relationship("Users", backref="reserves")
    room = relationship("Room", backref="reserves")


    def __init__(self, UserId, RoomId, Date, StartHour, EndHour):
        self.UserId = UserId
        self.RoomId = RoomId
        self.Date = Date
        self.StartHour = StartHour
        self.EndHour = EndHour


def addReserve(session, UserId, RoomId, Date, StartHour, EndHour):
    # Check if the UserId and RoomId exist in their respective tables
    user = session.query(Users).filter_by(id=UserId).first()
    room = session.query(Room).filter_by(id=RoomId).first()

    if not user:
        print(f"Error: User with id {UserId} does not exist.")
        return
    if not room:
        print(f"Error: Room with id {RoomId} does not exist.")
        return

    # Proceed with adding the reservation if both User and Room exist
    new_reserve = Reserve(UserId=UserId, RoomId=RoomId, Date=Date, StartHour=StartHour, EndHour=EndHour)
    session.add(new_reserve)
    try:
        session.commit()
        print("Reservation added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error while adding reservation: {e}")
