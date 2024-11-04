from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.database import Session  # Use the correct absolute import


class User(Base):
    __tablename__ = 'Users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    PositionId = Column(Integer, ForeignKey('Positions.id'), nullable=False)
    year = Column(Integer, nullable=True)
    
    position = relationship("Position", back_populates="users")
    reserves = relationship("Reserve", back_populates="user")

class UserDAL:
    def __init__(self, db_session: Session):  # type: ignore
        self.db_session = db_session

    def create_user(self, name: str, email: str, PositionId: int, year: int = None):
        new_user = User(name=name, email=email, PositionId=PositionId, year=year)
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)
        return new_user

    def get_user_by_id(self, user_id: int):
        return self.db_session.query(User).filter(User.id == user_id).first()

    def get_all_users(self):
        return self.db_session.query(User).all()

    def update_user(self, user_id: int, name: str = None, email: str = None, PositionId: int = None, year: int = None):
        user = self.get_user_by_id(user_id)
        if user:
            user.name = name if name else user.name
            user.email = email if email else user.email
            user.PositionId = PositionId if PositionId else user.PositionId
            user.year = year if year else user.year
            self.db_session.commit()
            self.db_session.refresh(user)
        return user

    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if user:
            self.db_session.delete(user)
            self.db_session.commit()
        return user

    def get_id_by_name(self, name: str) -> int:
        user = self.db_session.query(User).filter(User.name == name).first()
        return user.id if user else None