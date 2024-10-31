from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.database import Base, Session  # Import both Base and Session


class Position(Base):
    __tablename__ = 'Positions'
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    
    users = relationship("User", back_populates="position")

class PositionDAL:
    def __init__(self, db_session: Session):  # type: ignore
        self.db_session = db_session

    def get_position_by_id(self, position_id: int) -> Position:
        return self.db_session.query(Position).filter(Position.id == position_id).first()

    def get_all_positions(self) -> list[Position]:
        return self.db_session.query(Position).all()

    def create_position(self, name: str, position_id: int = None) -> Position:
        new_position = Position(id=position_id, name=name) if position_id else Position(name=name)
        self.db_session.add(new_position)
        self.db_session.commit()
        self.db_session.refresh(new_position)
        return new_position

    def update_position(self, position_id: int, name: str) -> Position:
        position = self.get_position_by_id(position_id)
        if position:
            position.name = name
            self.db_session.commit()
        return position

    def delete_position(self, position_id: int) -> bool:
        position = self.get_position_by_id(position_id)
        if position:
            self.db_session.delete(position)
            self.db_session.commit()
            return True
        return False