from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from werkzeug.security import generate_password_hash,check_password_hash
#from .models import User
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required,logout_user
from .models import User
from . import db
from datetime import date


#create a blueprint
bp = Blueprint('auth', __name__)

#for password storage
from werkzeug.security import generate_password_hash,check_password_hash

@bp.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    error=None
    if(form.validate_on_submit()==True):
        #get the username and password from the database
        user_name = form.user_name.data
        password = form.password.data
        u1 = User.query.filter_by(user_name=user_name).first()
        #if there is no user with that name
        if u1 is None:
            error='Incorrect user name'
        #check the password - notice password hash function
        elif not check_password_hash(u1.password_hash, password): # takes the hash and password
            error='Incorrect password'
        if error is None:
            #all good, set the login_user of flask_login to manage the user
            login_user(u1)
            flash('Logged in successfully!', 'info')
            return redirect(url_for('main.home'))
        else:
            flash(error)
    return render_template('user.html', form= form, heading='Login')

@bp.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    #the validation of form submis is fine
    if (form.validate_on_submit() == True):
            #get username, password and email from the form
            uname =form.user_name.data
            pwd = form.password.data
            email=form.email_id.data
            account_creation_date = date.today()
            #check if a user exists
            u1 = User.query.filter_by(user_name=uname).first()
            if u1:
                flash('User name already exists, please login')
                return redirect(url_for('auth.login'))
            # don't store the password - create password hash
            pwd_hash = generate_password_hash(pwd)
            #create a new user model object
            new_user = User(user_name=uname, password_hash=pwd_hash, email_id=email, account_creation_date = account_creation_date)
            db.session.add(new_user)
            db.session.commit()
            u1 = User.query.filter_by(user_name=uname).first()
            login_user(u1)
            #commit to the database and redirect to HTML page
            return redirect(url_for('main.home'))
    #the else is called when there is a get message
    else:
        return render_template('user.html', form=form, heading='Register')



@bp.route('/logout')
def logout():
    logout_user()
    flash('Logged out successfully!', 'info')
    return redirect(url_for('main.home'))
