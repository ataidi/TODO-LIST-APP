from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

path = "mysql+pymysql://root:Passeport#19@localhost/todo_db"


engine = create_engine(path)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()