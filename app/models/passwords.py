from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.database.database import Session 


class Password(Base):
    __tablename__ = 'Passwords'

    userId = Column(Integer, ForeignKey('Users.id'), primary_key=True)
    password = Column(String(255), nullable=False)

    user = relationship("User", back_populates="password")

class PasswordDAL:
    def __init__(self, db: Session): # type: ignore
        self.db = db

    def get_password_for_user(self, user_id: int):
        try:
            password_entry = self.db.query(Password).filter(Password.userId == user_id).first()
            if password_entry:
                print(f"Retrieved password for user ID = {user_id}")
            else:
                print(f"No password entry found for user ID = {user_id}")
            return password_entry
        except Exception as e:
            print(f"Error while fetching password for user ID {user_id}: {e}")
            raise


    def verify_password(self, user_id: int, password: str) -> bool:
        """Verify the provided password matches the stored password."""
        password_entry = self.get_password_for_user(user_id)
        if password_entry and password_entry.password == password:
            return True
        return False
