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

    def __json__ (self):
	dict_user = {}
	dict_user["id"] = self.id
	dict_user["username"] = self.username
 	dict_user["userid"] = self.userid
	dict_user["realname"] = self.realname
	dict_user["email"] = self.email
	dict_user["amount"] = self.amount
	return dict_user

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
    def __json__ (self):
        dict_keg = {}
        dict_keg["id"] = self.id
        dict_keg["kegid"] = self.kegid
        dict_keg["amount"] = self.amount
        return dict_keg

engine = create_engine('sqlite:///sqlalchemy_database.db')
Base.metadata.create_all(engine)
