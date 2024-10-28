import sqlalchemy
from sqlalchemy import Integer, Column
from sqlalchemy import create_engine, String

Base = sqlalchemy.orm.declarative_base()


# 1xx student number
# 2xx teacher number
class Position(Base):
    __tablename__ = 'Position'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __init__(self, name, id):
        self.id = id
        self.name = name

class PositionDAL:
    def __init__(self, session):
        self.session = session

    def addPosition(self, name, id):
        new_position = Position(name=name, id=id)
        self.session.add(new_position)
        self.session.commit()
        return new_position

    def getPosition(self, id):
        return self.session.query(Position).filter(Position.id == id).first()

    def getAllPositions(self):
        return self.session.query(Position).all()

    def updatePosition(self, id, new_name):
        position = self.get_position(id)
        if position:
            position.name = new_name
            self.session.commit()
        return position

    def deletePosition(self, id):
        position = self.get_position(id)
        if position:
            self.session.delete(position)
            self.session.commit()
        return position

# Example usage
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('your_database_url')
# Session = sessionmaker(bind=engine)
# session = Session()

# position_dal = PositionDAL(session)
# position_dal.add_position("Student", 100)
# position = position_dal.get_position(100)
# print(position)
# all_positions = position_dal.get_all_positions()
# print(all_positions)
# position_dal.update_position(100, "Updated Student")
# position_dal.delete_position(100)
# session.close()

