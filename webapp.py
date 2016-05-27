import sys
from flask import Flask, request
from flask import render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import User, Base

app = Flask(__name__)

def get_user():  #Retorna tots els usuaris i TOTA la seva informacio 
    engine = create_engine('sqlite:///sqlalchemy_database.db', echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    data = session.query(User.username, User.userid, User.email, User.realname, User.amount).all()
    return data

def get_amount(): #Retorna els usuaris i el amount
    engine = create_engine('sqlite:///sqlalchemy_database.db', echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    data = session.query(User.username, User.amount).all()
    return data

def save_user(username, userid, realname, email): #Crear usuari
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    ed_user = User(username, userid, realname, email, amount=0.0)
    session.add(ed_user)
    session.commit()

def delete_user(username): #Esborrar usuari
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    ed_user = session.query(User).filter_by(username=username).one()
    session.delete(ed_user)
    session.commit()

def update_user(username, userid, realname, email, amount): #Actualitzar usuari
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSesion()
    ed_user = session.query(User).filter_by(username_username).one()
    ed_user.userid = userid
    ed_user.realname = realname
    ed_user.email = email
    ed_user.amount = amount
    session.commit()

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



#Home Page.
@app.route('/')
def index():
    return render_template('index.html')

#Gestio d'usuaris.
@app.route('/users_management')
def users_management():
    return render_template('users_management.html')

#Gestio d'usuaris (CREATE).
@app.route('/create_user', methods=['GET','POST'])
def create_user():
    if request.method == 'GET':
        return render_template('create_user.html')
    elif request.method == 'POST':
	username = request.form.get('username')
	userid = request.form.get('userid')
        realname = request.form.get('realname')
	email = request.form.get('email')
	save_user(username, userid, realname, email)
	return 'OK'
	#Afegir user registered correctly / error

#Gestio d'usuaris (DELETE).
@app.route('/users_management/delete_user', methods=['GET','POST'])
def delete_user():
#    data = #get ??
    if request.method == 'GET':
	return render_template('delete_user.html',data = data)
    elif request.method == 'POST':
	username = request.form.get('username')
	delete_user(username)
	return "Delete user correctly?"
	#Afegir user deleted correctly or error!!!	

#Gestio d'usuaris (UPDATE).
@app.route('/users_management/update_user', methods=['GET','POST'])
def update_user():
 #   data = #get  ????
    if request.method == 'GET':
	return render_template('update_user.html', data=data)
    elif request.method == 'POST':
 	username = request.form.get('username')
	userid = request.form.get('userid')
	realname = request.form.get('realname')
	email = request.form.get('email')
	amount = request.form.get('amount')
	update_user(username, userid, realname, email, amount)
	return "Update user correctly?"
	#Afegir correctly/error

#Mostrar tots els usuaris i els amounts.
@app.route('/show_users')
def show_users():
    data = get_amount()
    return render_template('show_user_table.html', data=data)

#Gestio de surtidors
@app.route('/kegs_management')
def kegs_management():
    return render_temp







if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")




