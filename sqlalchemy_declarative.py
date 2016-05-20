from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    userid = Column(String)
    realname = Column(String)
    email = Column(String)
    amount = Column(Float)

    def __init__(self, username, userid, realname, email, amount):
        self.username = username
	self.userid = userid
        self.realname = realname
        self.email = email
        self.amount = amount

    def __repr__(self):
        return "<User(username='%s', userid='%s', realname='%s', email='%s', amount='%d')>" % (
                        self.username, self.userid, self.realname, self.email, self.amount)

class Keg(Base):
    __tablename__ = 'keg'
    id = Column(Integer, primary_key=True)
    kegid = Column(String)
    amount = Column(Float)

    def __init__(self, kegid, amount):
        self.kegid = kegid
        self.amount = amount

    def __repr__(self):
        return "<Keg(kegid='%s',amount='%d')>" % (
                        self.kegid, self.amount)

engine = create_engine('sqlite:///sqlalchemy_database.db')
Base.metadata.create_all(engine)
