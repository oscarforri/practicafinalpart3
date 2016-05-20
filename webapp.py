import sys
from flask import Flask, request
from flask import render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import User, Base

app = Flask(__name__)


#Home Page.
@app.route('/')
def index():
    return render_template('index.html')

#Gestio d'usuaris.
@app.route('/users_management')
def users_management():
    return render_template('users_management.html')

#Gestio d'usuaris (CREATE).
@app.route('/users_management/create_user', methods=['GET','POST'])
def create_user():
    if request.method == 'GET':
        return render_template('create_user.html')
    elif request.method == 'POST':
	#username = request.form.get('username')
	#userid = request.form.get('userid')
        #realname = request.form.get('realname')
	#email = request.form.get('email')
	#save_userORM(username,fullname,email,password)
	return render_template('OK')

#Gestio d'usuaris (DELETE).
@app.route('/users_management/delete_user')
def delete_user():
    return render_template('delete_user.html')

#Gestio d'usuaris (UPDATE).
@app.route('/update_user')
def update_user():
    return render_template('update_user.html')

#Gestio de surtidors
@app.route('/kegs_management')
def kegs_management():
    return render_template('kegs_management.html')

#Mostrar tots els usuaris.
@app.route('/show_users')
def show_users():
    return "Mostrar tots els usuaris"

#Mostrar tots els surtidors.
@app.route('/show_kegs')
def show_kegs():
    return "Mostrar tots els sortidors"


if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")




