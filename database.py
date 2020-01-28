from model import *

from sqlalchemy.pool import SingletonThreadPool

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# replace lecture.db with your own database file
engine = create_engine('sqlite:///database.db',poolclass=SingletonThreadPool, connect_args={'check_same_thread':False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user( password, name):
    user = User(
        password=password,
        name=name,
        )
    print("hello")
    session.add(user)
    session.commit()

def update_password(id, password):
   user_object = session.query(
       User).filter_by(
       id=id).first()
   user_object.password = password
   session.commit()

def delete_user(their_id):
   session.query(User).filter_by(
       id=their_id).delete()
   session.commit()

def query_all():
   users = session.query(
      User).all()
   return users

def query_by_id(their_id):
   user = session.query(
       User).filter_by(
       id=their_id).first()
   return user