from sqlalchemy import Column, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.database.database import Session  # Use the correct absolute import
from datetime import date,time


class Reserve(Base):
    __tablename__ = 'Reserves'
    
    ReserveId = Column(Integer, primary_key=True, autoincrement=True)
    UserId = Column(Integer, ForeignKey('Users.id'), nullable=False)
    RoomId = Column(Integer, ForeignKey('Rooms.id'), nullable=False)
    Date = Column(Date, nullable=False)
    StartHour = Column(Time, nullable=False)
    EndHour = Column(Time, nullable=False)
    
    user = relationship("User", back_populates="reserves")
    room = relationship("Room", back_populates="reserves")

class ReserveDAL:
    def __init__(self, session: Session):  # type: ignore
        self.session = session

    def create_reserve(self, user_id: int, room_id: int, reserve_date: date, start_hour: time, end_hour: time) -> Reserve:
        new_reserve = Reserve(
            UserId=user_id,
            RoomId=room_id,
            Date=reserve_date,
            StartHour=start_hour,
            EndHour=end_hour
        )
        self.session.add(new_reserve)
        self.session.commit()
        self.session.refresh(new_reserve)
        return new_reserve

    def get_reserve_by_id(self, reserve_id: int) -> Reserve:
        return self.session.query(Reserve).filter(Reserve.ReserveId == reserve_id).first()

    def get_reserves_by_user(self, user_id: int) -> list[Reserve]:
        return self.session.query(Reserve).filter(Reserve.UserId == user_id).all()

    def get_reserves_by_room_and_date(self, room_id: int, reserve_date: date) -> list[Reserve]:
        return self.session.query(Reserve).filter(Reserve.RoomId == room_id, Reserve.Date == reserve_date).all()

    def update_reserve(self, reserve_id: int, start_hour: time, end_hour: time) -> bool:
        reserve = self.get_reserve_by_id(reserve_id)
        if reserve:
            reserve.StartHour = start_hour
            reserve.EndHour = end_hour
            self.session.commit()
            return True
        return False

    def delete_reserve(self, reserve_id: int) -> bool:
        reserve = self.get_reserve_by_id(reserve_id)
        if reserve:
            self.session.delete(reserve)
            self.session.commit()
            return True
        return False

    def get_all_reserves(self) -> list[Reserve]:  # This is the method you're looking for
        return self.session.query(Reserve).all()
    
    def update_reserve(self, reserve_id: int, **kwargs) -> bool:
        reserve = self.get_reserve_by_id(reserve_id)
        if reserve:
            # Update fields only if provided in kwargs
            if "user_id" in kwargs and kwargs["user_id"] is not None:
                reserve.UserId = kwargs["user_id"]
            if "room_id" in kwargs and kwargs["room_id"] is not None:
                reserve.RoomId = kwargs["room_id"]
            if "date" in kwargs and kwargs["date"] is not None:
                reserve.Date = kwargs["date"]
            if "start_hour" in kwargs and kwargs["start_hour"] is not None:
                reserve.StartHour = kwargs["start_hour"]
            if "end_hour" in kwargs and kwargs["end_hour"] is not None:
                reserve.EndHour = kwargs["end_hour"]
            
            # Commit changes to the database and refresh the instance
            self.session.commit()
            self.session.refresh(reserve)
            return True
        return False