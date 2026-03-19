from sqlalchemy import Column, Integer, String
from connections import Base

class Todo(Base):
    __tablename__="todo_tbl"
    id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(String(100))
    description=Column(String(100))
    