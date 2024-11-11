from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from app.database import Base
from app.database import Session  # Use the correct absolute import


class Room(Base):
    __tablename__ = 'Rooms'
    
    id = Column(Integer, primary_key=True)
    reserves = relationship("Reserve", back_populates="room")



class RoomDAL:
    def __init__(self, session: Session):  # type: ignore
        self.session = session

    def create_room(self, room_id: int) -> Room:
        new_room = Room(id=room_id)
        self.session.add(new_room)
        self.session.commit()
        self.session.refresh(new_room)
        return new_room

    def get_all_rooms(self) -> list[Room]:
        rooms = self.session.query(Room).all()
        if rooms:
            print("All room IDs:")
            for room in rooms:
                print(f"- ID: {room.id}")
        else:
            print("No rooms found.")
        return rooms

    def delete_room(self, room_id: int) -> bool:
        room = self.session.query(Room).filter(Room.id == room_id).first()
        if room:
            self.session.delete(room)
            self.session.commit()
            return True
        else:
            return False


