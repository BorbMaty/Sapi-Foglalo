from firebase_admin import db

class PositionDAL:
    def __init__(self):
        self.ref = db.reference('positions')

    # def get_position_by_id(self, position_id: int) -> Position:
    #     return self.db_session.query(Position).filter(Position.id == position_id).first()

    # def get_all_positions(self) -> list[Position]:
    #     return self.db_session.query(Position).all()

    def create_position(self, name):
        new_position_ref = self.ref.push()  # Automatically generates a unique ID
        new_position_ref.set({
            'name': name
        })
        return new_position_ref.key  # Returns the Firebase-generated ID

    # def update_position(self, position_id: int, name: str) -> Position:
    #     position = self.get_position_by_id(position_id)
    #     if position:
    #         position.name = name
    #         self.db_session.commit()
    #     return position

    # def delete_position(self, position_id: int) -> bool:
    #     position = self.get_position_by_id(position_id)
    #     if position:
    #         self.db_session.delete(position)
    #         self.db_session.commit()
    #         return True
    #     return False