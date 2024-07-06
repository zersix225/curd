from sqlalchemy import Column, Integer, String
from db import Base
 
# Define ToDo class from Base
class Mybook(Base):
    __tablename__ = 'Mybook'
    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    author = Column(String(256))
    description = Column(String(256))