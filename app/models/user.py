from firebase_admin import db

class UserDAL:
    def __init__(self):
        self.ref = db.reference('users')

    def create_user(self, name, email, position_id, room_id):
        new_user_ref = self.ref.push()
        new_user_ref.set({
            'name': name,
            'email': email,
            'position_id': position_id,
            'room_id': room_id
        })
        return new_user_ref.key

    # def get_user_by_id(self, user_id: int):
    #     return self.db_session.query(User).filter(User.id == user_id).first()

    # def get_all_users(self):
    #     return self.db_session.query(User).all()

    # def update_user(self, user_id: int, name: str = None, email: str = None, PositionId: int = None, year: int = None):
    #     user = self.get_user_by_id(user_id)
    #     if user:
    #         user.name = name if name else user.name
    #         user.email = email if email else user.email
    #         user.PositionId = PositionId if PositionId else user.PositionId
    #         user.year = year if year else user.year
    #         self.db_session.commit()
    #         self.db_session.refresh(user)
    #     return user

    # def delete_user(self, user_id: int):
    #     user = self.get_user_by_id(user_id)
    #     if user:
    #         self.db_session.delete(user)
    #         self.db_session.commit()
    #     return user