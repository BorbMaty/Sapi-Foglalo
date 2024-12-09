from sqlalchemy import Column, Integer, Date, Time, ForeignKey, and_
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.database.database import Session  # Use the correct absolute import
from datetime import date,time
from app.models.user import User

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

    from datetime import time
    from sqlalchemy import and_

    from datetime import date, time

    def is_free_in_this_interval(self, room_id: int, reserve_date: date, start_time: time, end_time: time) -> bool:
        conflict = self.session.query(Reserve).filter(
            Reserve.RoomId == room_id,
            Reserve.Date == reserve_date,
            and_(
                Reserve.StartHour < end_time,
                Reserve.EndHour > start_time
            )
        ).first()

        return conflict is None

    def create_reserve(self, user_id: int, room_id: int, reserve_date: date, start_hour: time,
                       end_hour: time) -> Reserve:
        if self.is_free_in_this_interval(room_id, reserve_date, start_hour, end_hour):
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
        else:
            print(f"Room {room_id} is already reserved on {reserve_date} between {start_hour} and {end_hour}.")
            return None

    def get_reserve_by_id(self, reserve_id: int) -> Reserve:
        reserve = self.session.query(Reserve).filter(Reserve.ReserveId == reserve_id).first()
        if reserve:
            print(
                f"Reserve with ID {reserve.ReserveId}:\n- User ID: {reserve.UserId}\n- Room ID: {reserve.RoomId}\n- Date: {reserve.Date}\n- Start Hour: {reserve.StartHour}\n- End Hour: {reserve.EndHour}")
        else:
            print(f"No reserve found with ID {reserve_id}.")
        return reserve

    def get_reserves_by_user(self, user_id: int) -> list[Reserve]:
        reserves = self.session.query(Reserve).filter(Reserve.UserId == user_id).all()
        if reserves:
            print(f"Reserves for User ID {user_id}:")
            for reserve in reserves:
                print(
                    f"- Reserve ID: {reserve.ReserveId}, Room ID: {reserve.RoomId}, Date: {reserve.Date}, Start: {reserve.StartHour}, End: {reserve.EndHour}")
        else:
            print(f"No reserves found for User ID {user_id}.")
        return reserves

    def get_reserves_by_room_and_date(self, room_id: int, reserve_date: date) -> list[Reserve]:
        reserves = self.session.query(Reserve).filter(Reserve.RoomId == room_id, Reserve.Date == reserve_date).all()
        if reserves:
            print(f"Reserves for Room ID {room_id} on {reserve_date}:")
            for reserve in reserves:
                print(
                    f"- Reserve ID: {reserve.ReserveId}, User ID: {reserve.UserId}, Start: {reserve.StartHour}, End: {reserve.EndHour}")
        else:
            print(f"No reserves found for Room ID {room_id} on {reserve_date}.")
        return reserves

    def update_reserve(self, reserve_id: int, start_hour: time, end_hour: time) -> bool:
        reserve = self.get_reserve_by_id(reserve_id)
        if reserve:
            reserve.StartHour = start_hour
            reserve.EndHour = end_hour
            self.session.commit()
            return True
        return False

    def delete_reserve_by_id(self, reserve_id: int) -> bool:
        print("Deleted reservation:")
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
    
    def get_conflicting_reserve(self, room_id, reserve_date, start_hour, end_hour):
        return self.db.query(Reserve).filter(
            Reserve.room_id == room_id,
            Reserve.reserve_date == reserve_date,
            Reserve.start_hour < end_hour,  # Check overlapping times
            Reserve.end_hour > start_hour
        ).first()
    
    def get_reserves_by_username(self, username: str) -> list[Reserve]:
        # This performs the equivalent of:
        # SELECT r.ReserveId, r.UserId, r.RoomId, r.Date, r.StartHour, r.EndHour
        # FROM Reserves AS r
        # JOIN Users AS u ON r.UserId = u.id
        # WHERE u.name = :username
        reserves = (
            self.session.query(Reserve)
            .join(Reserve.user)  # join to the User table via the relationship
            .filter(User.name == username)
            .all()
        )
        
        # Optional: print out the results for debugging
        if reserves:
            print(f"Reserves for user '{username}':")
            for reserve in reserves:
                print(f"- Reserve ID: {reserve.ReserveId}, Room ID: {reserve.RoomId}, Date: {reserve.Date}, "
                      f"Start: {reserve.StartHour}, End: {reserve.EndHour}")
        else:
            print(f"No reserves found for user '{username}'.")

        return reserves