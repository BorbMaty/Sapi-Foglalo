from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.database.database import Session  # Use the correct absolute import


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
        # Retrieve the User instance by ID
        user = self.db_session.query(User).filter(User.id == user_id).first()
        if user:
            print(f"User with ID {user.id} found. Name = {user.name}")
        else:
            print(f"No user found with ID {user_id}.")
        return user

    def get_all_users(self):
        # Retrieve all User instances
        users = self.db_session.query(User).all()
        if users:
            print("All users:")
            for user in users:
                print(f"- ID: {user.id}")
        else:
            print("No users found.")
        return users

    def update_user(self, user_id: int, name: str = None, email: str = None, PositionId: int = None, year: int = None):
        user = self.get_user_by_id(user_id)
        if user:
            # Make sure each field is updated individually without concatenation
            if name is not None:
                user.name = name
            if email is not None:
                user.email = email
            if PositionId is not None:
                user.PositionId = PositionId
            if year is not None:
                user.year = year

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
    
    def get_user_by_email(self, email: str) -> User:
        return self.db_session.query(User).filter(User.email == email).first()