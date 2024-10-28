import sqlalchemy
from sqlalchemy import Integer, Column
from sqlalchemy import create_engine, String
from sqlalchemy.orm import relationship

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    position = Column(String, nullable=False)
    year = Column(Integer, nullable=True)

    reservations = relationship('Reserves', backref='User') 

    def __init__(self, name, email, position, year=None):
        self.name = name
        self.email = email
        self.position = position
        self.year = year

    def addUser(session, name, email, position, year=None):
        new_user = User(name=name, email=email, position=position, year=year)
        session.add(new_user)
        session.commit()
        print(f"New user. Name: {name}, e-mail: {email}, position: {position}, year : {year}")

    def deleteUserByID(session, user_id):
        user_to_delete = session.query(User).filter(User.id == user_id).first()

        if user_to_delete:
            session.delete(user_to_delete)
            session.commit()
            print(f"Deleted user: {user_to_delete.name} ({user_to_delete.email})")
        else:
            # TODO: add logging.debug/warning
            print(f"No user with this id: {user_id}")

            # TODO: add custom exception
            # Create a custom exception from Exception class
            # raise UserNotFoundException("Sorry, no numbers below zero")

    def getUserNameByID(session, user_id):
        user = session.query(User).filter(User.id == user_id).first()

        if user:
            return user.name
        else:
            return "Nincs ilyen felhasználó"