from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///first_PU.db', echo=True)
Base = declarative_base()

########################################################################
class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    name = Column(String)

#----------------------------------------------------------------------
    def __init__(self, username, password, name):

        self.username = username
        self.password = password
        self.name = name

        # create tables
Base.metadata.create_all(engine)