from datetime import date,time

from firebase_admin import db

import app.database

class ReserveDAL:
    def __init__(self):
        self.ref = db.reference('reserves')

    def create_reserve(self, user_id: int, room_id: int, reserve_date: date, start_hour: time, end_hour: time) -> str:
        new_reserve_ref = self.ref.push()
        new_reserve_ref.set({
            'user_id': user_id,
            'room_id': room_id,
            'reserve_date': reserve_date.isoformat(),
            'start_hour': start_hour.isoformat(),
            'end_hour': end_hour.isoformat()
        })
        return new_reserve_ref.key

    # def get_reserve_by_id(self, reserve_id: int) -> Reserve:
    #     return self.session.query(Reserve).filter(Reserve.ReserveId == reserve_id).first()

    # def get_reserves_by_user(self, user_id: int) -> list[Reserve]:
    #     return self.session.query(Reserve).filter(Reserve.UserId == user_id).all()

    # def get_reserves_by_room_and_date(self, room_id: int, reserve_date: date) -> list[Reserve]:
    #     return self.session.query(Reserve).filter(Reserve.RoomId == room_id, Reserve.Date == reserve_date).all()

    # def update_reserve(self, reserve_id: int, start_hour: time, end_hour: time) -> bool:
    #     reserve = self.get_reserve_by_id(reserve_id)
    #     if reserve:
    #         reserve.StartHour = start_hour
    #         reserve.EndHour = end_hour
    #         self.session.commit()
    #         return True
    #     return False

    # def delete_reserve(self, reserve_id: int) -> bool:
    #     reserve = self.get_reserve_by_id(reserve_id)
    #     if reserve:
    #         self.session.delete(reserve)
    #         self.session.commit()
    #         return True
    #     return False
