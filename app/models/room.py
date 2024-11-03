# from sqlalchemy import Column, Integer
# from sqlalchemy.orm import relationship
# from app.database import Base
# from app.database import Session  # Use the correct absolute import

from firebase_admin import db

class RoomDAL:
    def __init__(self):
        self.ref = db.reference('rooms')

    def create_room(self, room_number):
        new_room_ref = self.ref.push()
        new_room_ref.set({
            'room_number': room_number
        })
        return new_room_ref.key

    # def get_room_by_id(self, room_id: int) -> Room:
    #     return self.session.query(Room).filter(Room.id == room_id).first()

    # def get_all_rooms(self) -> list[Room]:
    #     return self.session.query(Room).all()

    # def delete_room(self, room_id: int) -> bool:
    #     room = self.get_room_by_id(room_id)
    #     if room:
    #         self.session.delete(room)
    #         self.session.commit()
    #         return True
    #     return False

