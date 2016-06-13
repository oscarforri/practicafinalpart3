import sys
from flask import Flask, request, jsonify, abort, make_response
from flask import render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import User, Base, Keg

app = Flask(__name__)

#USER functions:
def get_user(username):  #Retorna tots els usuaris i TOTA la seva informacio 
    engine = create_engine('sqlite:///sqlalchemy_database.db', echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    data = session.query(User.username, User.userid, User.email, User.realname, User.amount).filter_by(username=username).all()
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
    try:
    	ed_user = session.query(User).filter_by(username=username).one()
    	session.delete(ed_user)
    	session.commit()
       	return True
    except:
	return False

def update_user(username, userid, realname, email, amount): #Actualitzar usuari
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
    	ed_user = session.query(User).filter_by(username=username).one()  
	ed_user.userid = userid
    	ed_user.realname = realname
    	ed_user.email = email
    	ed_user.amount = amount
    	session.commit()
	return True
    except:
	return False

def exist_user(username):   #Comprovar si existeix l'usuari
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try: 
	ed_user = session.query(User).filter_by(username=username).one()
        return True
    except:
	return False	

#KEG functions:
def get_kegs():
    engine = create_engine('sqlite:///sqlalchemy_database.db', echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    data = session.query(Keg.kegid, Keg.amount).all()
    return data

def get_keg(kegid):  #Retorna tots els usuaris i TOTA la seva informacio 
    engine = create_engine('sqlite:///sqlalchemy_database.db', echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    data = session.query(Keg.kegid,Keg.amount).filter_by(kegid=kegid).all()
    return data


def save_keg(kegid):
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    ed_keg = Keg(kegid,amount=0.0)
    session.add(ed_keg)
    session.commit()

def delete_keg(kegid): #Eliminar Keg
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
	ed_keg = session.query(Keg).filter_by(kegid=kegid).one()
    	session.delete(ed_keg)
    	session.commit()
	return True
    except:
	return False

def update_keg(kegid, amount): #Actualitzar Keg
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
    	ed_keg = session.query(Keg).filter_by(kegid=kegid).one()
      	ed_keg.amount = amount
    	session.commit()
	return True
    except:
	return False




def exist_keg():
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try: 
	ed_keg = session.query(Keg).filter_by(kegid=kegid).one()
        return True
    except:
	return False	

####################################################################

#Error (JSON WebServices).
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

#Home Page.
@app.route('/')
def index():
    return render_template('index.html')

#WebServer main page.
@app.route('/ws')
def index_ws(): 
    return render_template('index_ws.html')

#WebApp main page. 
@app.route('/wa')
def index_wa():
    return render_template('index_wa.html')

#####################__CREATE__########################################

#WebApp Gestio d'usuaris (CREATE).
@app.route('/wa/create_user', methods=['GET','POST'])
def create_user_wa():
    if request.method == 'GET':
        return render_template('create_user.html')
    elif request.method == 'POST':
	username = request.form.get('username')
	userid = request.form.get('userid')
        realname = request.form.get('realname')
	email = request.form.get('email')
	save_user(username, userid, realname, email)
	return render_template('create_correctly.html')

#WebApp Gestio de kegs (CREATE).
@app.route('/wa/create_keg',methods=['GET','POST'])
def create_keg_wa():
    if request.method == 'GET':
	return render_template('create_keg.html')
    elif request.method == 'POST':
	kegid = request.form.get('kegid')
	save_keg(kegid)
	return render_template("create_correctly.html")

#WebServer Gestio d'usuaris (CREATE).
@app.route('/ws/users', methods=['POST'])
def create_user_ws():
    if not request.json or not 'username' in request.json or not 'userid' in request.json or not 'realname' in request.json or not 'email' in request.json:
        abort(400)
    if exist_user(request.json['username']):
	abort(400)
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
	ed_user = User(username=request.json['username'],userid=request.json['userid'],realname=request.json['realname'],email=request.json['email'], amount=0.0)
	session.add(ed_user)
	session.commit()
    except:
	abort(404)    
    return jsonify(id=ed_user.id,username=ed_user.username,userid=ed_user.userid,realname=ed_user.realname,email=ed_user.email,amount=ed_user.amount)

#WebServer Gestio de kegs (CREATE).
@app.route('/ws/kegs', methods=['POST'])


###########################################################################

#WebApp Gestio d'usuaris (READ).
@app.route('/wa/show_users')
def show_users_wa():
    data = get_amount()
    return render_template('show_user_table.html', data=data)

@app.route('/wa/user/<username>', methods=['GET','POST'])
def read_user_wa(username):
    data = get_user(username)
    return render_template('edit_user.html', data=data)

#WebApp Gestio de kegs (READ).
@app.route('/wa/show_kegs')
def show_kegs_wa():
    data = get_kegs()
    return render_template('show_keg_table.html', data=data)

#@app.route('/wa/keg/<kegid>', methods=['GET','POST'])
#def show_kegs_wa(kegid):
 #   data = get_keg(kegid)
#    return render_template('edit_keg.html', data=data)

@app.route('/wa/keg/<kegid>', methods=['GET', 'POST'])
def show_keg_wa(kegid):
    data = get_keg(kegid)
    return render_template('edit_keg.html',data=data)





#WebServer Gestio d'usuaris (READ).
@app.route('/ws/users', methods=['GET'])  #READ ALL USER
def show_users_ws():
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    users = session.query(User).all()
    all_users = [ user.__json__() for user in users]
    session.commit()
    return jsonify({'users': all_users})

@app.route('/ws/users/<username>', methods=['GET'])
def show_user_ws(username):
    engine = create_engine('sqlite:///sqlalchemy_database.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
        ed_user = session.query(User).filter_by(username=username).one()
        session.commit()
    except:
        abort(404)
    return jsonify(id=ed_user.id,username=ed_user.username,userid=ed_user.userid,realname=ed_user.realname,email=ed_user.email,amount=ed_user.amount)

########################################################################

#WebApp Gestio d'usuaris (UPDATE).
@app.route('/wa/update_user', methods=['POST'])
def update_user_wa():
        username = request.form.get('user_name')
        userid = request.form.get('userid')
        realname = request.form.get('realname')
        email = request.form.get('email')
        amount = request.form.get('amount')
        if update_user(username, userid, realname, email, amount):
          return render_template('update_correctly.html')
      	else:
 	  return render_template('update_error.html')

#WebApp Gestio de kegs (UPDATE).
@app.route('/wa/update_keg', methods=['POST'])
def update_keg_wa():
	kegid = request.form.get('kegid')
  	amount = request.form.get('amount')
       	if update_keg(kegid, amount):
	  return render_template('update_correctly.html')
      	else:
	  return render_template('update_error.html')

#WebServer Gestio d'usuaris (UPDATE).
#@app.route('/ws/user/', methods=['POST']


#########################################################################

#WebApp Gestio d'usuaris (DELETE).
@app.route('/wa/delete_user', methods=['POST'])
def delete_user_wa():
    username = request.form.get('username')
    if delete_user(username):
     	return render_template('delete_correctly.html')
    else:
	return render_template('delete_error.html')

#WebApp Gestio de kegs (DELET).
@app.route('/wa/delete_keg', methods=['POST'])
def delete_keg_wa():
    kegid = request.form.get('kegid')
    if delete_keg(kegid):
	return render_template('delete_correctly.html')
    else:
        return render_template('delete_error.html')



########################################################################






#Gestio de surtidors
@app.route('/wa/kegs_management')
def kegs_management():
    return render_temp







if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")




