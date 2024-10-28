import sqlalchemy
from sqlalchemy import Integer, Column
from sqlalchemy import create_engine, String

Base = sqlalchemy.orm.declarative_base()



# 1xx student number
# 2xx teacher number
class Position(Base):
    __tablename__ = 'Positions'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __init__(self, name, id):
        self.id = id
        self.name = name

    def addPosition(session, name, id):
        new_position = Position(name=name, id=id)
        session.add(new_position)
        session.commit()
