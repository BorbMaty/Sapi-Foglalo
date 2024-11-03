# import sqlalchemy
# from sqlalchemy import Integer, Column, ForeignKey, Date, Time
# from sqlalchemy.orm import relationship

# Base = sqlalchemy.orm.declarative_base()

# class Reserve(Base):
#     __tablename__ = 'Reserves'

#     ReserveId = Column(Integer, primary_key=True, autoincrement=True)
#     UserId = Column(Integer, ForeignKey('users.id'), nullable=False)
#     RoomId = Column(Integer, ForeignKey('rooms.id'), nullable=False)
#     Date = Column(Date, nullable=False)
#     StartHour = Column(Time, nullable=False)
#     EndHour = Column(Time, nullable=False)

#     users = relationship('User', backref='Reserve')
#     rooms = relationship('Room', backref='Reserve')

#     def __init__(self, UserId, RoomId, Date, StartHour, EndHour):
#         self.UserId = UserId
#         self.RoomId = RoomId
#         self.Date = Date
#         self.StartHour = StartHour
#         self.EndHour = EndHour


# class ReserveDAL:
#     def __init__(self, session):
#         self.session = session

#     def addReserve(self, user_id, room_id, date, start_hour, end_hour):
#         reservation = Reserve(user_id, room_id, date, start_hour, end_hour)
#         self.session.add(reservation)
#         self.session.commit()
#         return reservation

#     def getReserve(self, ReserveId):
#         return self.session.query(Reserve).filter(Reserve.ReserveId == ReserveId).first()

#     def getAllReserves(self):
#         return self.session.query(Reserve).all()

#     def updateReserve(self, ReserveId, UserId=None, RoomId=None, Date=None, StartHour=None, EndHour=None):
#         reserve = self.get_reserve(ReserveId)
#         if reserve:
#             if UserId is not None:
#                 reserve.UserId = UserId
#             if RoomId is not None:
#                 reserve.RoomId = RoomId
#             if Date is not None:
#                 reserve.Date = Date
#             if StartHour is not None:
#                 reserve.StartHour = StartHour
#             if EndHour is not None:
#                 reserve.EndHour = EndHour
#             self.session.commit()
#         return reserve

#     def deleteReserve(self, ReserveId):
#         reserve = self.get_reserve(ReserveId)
#         if reserve:
#             self.session.delete(reserve)
#             self.session.commit()
#         return reserve

# # Example usage
# # from sqlalchemy import create_engine
# # from sqlalchemy.orm import sessionmaker

# # engine = create_engine('your_database_url')
# # Session = sessionmaker(bind=engine)
# # session = Session()

# # reserve_dal = ReserveDAL(session)
# # reserve_dal.add_reserve(UserId=1, RoomId=2, Date='2024-10-30', StartHour='09:00:00', EndHour='10:00:00')
# # reserve = reserve_dal.get_reserve(1)
# # print(reserve)
# # all_reserves = reserve_dal.get_all_reserves()
# # print(all_reserves)
# # reserve_dal.update_reserve(1, EndHour='11:00:00')
# # reserve_dal.delete_reserve(1)
# # session.close()