from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import User, Base

def get_user():
    engine = create_engine('sqlite:///sqlalchemy_database.db', echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    data = session.query(User.username, User.userid, User.realname, User.email, User.amount).all()
    return data

def save_user(username, userid, realname, email, amount):
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    ed_user = User(uusername, userid, realname, email, amount)
    session.add(ed_user)
    session.commit()

def delete_user():
    pass
    
def update_user():
    pass

def get_keg():
    engine = create_engine('sqlite:///sqlalchemy_database.db', echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    data = session.query(Keg.kegid, Keg.amount).all()
    return data

def save_keg(kegid, amount):
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    ed_keg = User(kegid, amount)
    session.add(ed_keg)
    session.commit()

def delete_keg():
    pass
    
def update_keg():
    pass

