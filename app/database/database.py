from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "mysql+pymysql://mara:alma@localhost/testDB"
# DATABASE_URL = 'mysql+mysqlconnector://root:1234@localhost:3306/testDB'
DATABASE_URL = 'mssql+pyodbc://room-reserver-admin:Correct-Horse-Battery-Staple!@sql-room-reserver.database.windows.net:1433/testDB?driver=ODBC+Driver+17+for+SQL+Server'


engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()