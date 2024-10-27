import sqlalchemy
from sqlalchemy import Integer, Column
from sqlalchemy import create_engine, String

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    position = Column(String, nullable=False)
    year = Column(Integer, nullable=True)

    def __init__(self, name, email, position, year=None):
        self.name = name
        self.email = email
        self.position = position
        self.year = year

    def addUser(session, name, email, position, year=None):
        # Új felhasználó hozzáadása az adatbázishoz.
        new_user = User(name=name, email=email, position=position, year=year)
        session.add(new_user)
        session.commit()
        print(f"New user. Name: {name}, e-mail: {email}, position: {position}, year : {year}")

    def deleteUserByID(session, user_id):
        # id szerinti felhasználó törlés
        user_to_delete = session.query(User).filter(User.id == user_id).first()

        if user_to_delete:
            session.delete(user_to_delete)
            session.commit()
            print(f"Deleted user: {user_to_delete.name} ({user_to_delete.email})")
        else:
            print(f"No user with this id: {user_id}")

    def getUserNameByID(session, user_id):
        # Felhasználó keresése az ID alapján
        user = session.query(User).filter(User.id == user_id).first()

        if user:
            return user.name
        else:
            return "Nincs ilyen felhasználó"

