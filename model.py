from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class User(Base):
   __tablename__ = 'user'
   id = Column(Integer, primary_key=True)
  
   name = Column(String)
   password = Column(String)


class Music(Base):
   __tablename__ = 'song'
   id = Column(Integer, primary_key=True)
   file_name=Column(String)

   #table name files , add all the songs for: {%}