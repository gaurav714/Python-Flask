## LOGIN features
from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_login import login_user, logout_user, login_required

##For storing password as hash
from werkzeug.security import generate_password_hash, check_password_hash

from .models import user

## by giving filename _init__ it tells python that the module is a package and all the functions are available to use within the directory
from . import db

## __name__ represents the name of the current file, it ensures Blueprint can find its resources relative to the file
## location
auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template('login.html')
@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup',methods=['POST'])
def signup_post():
    name=request.form.get('inputName')
    email=request.form.get('exampleInputEmail1')
    password=request.form.get('exampleInputPassword1')
    print(name,email,password)

    UserAlreadyPresent=user.query.filter_by(email=email).first()
    if UserAlreadyPresent:
        flash('Email address already exists')
        print("user already present!!!")
        return redirect(url_for('auth.login'))
    
    else:
        new_user=user(name=name, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        try:
            db.session.commit()
            flash('User created successfully!')
            print('User created successfully!')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash('Error creating user')
            print(f'Error creating user: {e}')
            return redirect(url_for('auth.signup'))
            # Handle the error appropriately (e.g., rollback the session)


 ## Implement Flask-Login for uses session management           
@auth.route('/login',methods=['POST'])
def login_post():
    name=request.form.get('inputName')
    email=request.form.get('exampleInputEmail1')
    password=request.form.get('exampleInputPassword1')
    rem =True if request.form.get('remember') else False

    #checking if the user exists or the password is incorrect
    UserExists= user.query.filter_by(email=email).first()

    if not UserExists:
        print ("user does not exist please signup first")
        flash('User does not exist please signup first')
        return redirect(url_for('auth.signup'))
    elif UserExists and not check_password_hash(UserExists.password, password):
        print ("password is incorrect")
        flash('password is incorrect')
        return redirect(url_for('auth.login'))
    else:
        login_user(UserExists, remember=rem)
        flash('Logged in successfully!')
        return redirect(url_for('main.profile'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    print ('logged out')
    return redirect(url_for('main.index'))