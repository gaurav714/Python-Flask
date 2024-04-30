## LOGIN features
from flask import Blueprint, render_template, url_for, request, redirect

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
    return redirect (url_for('auth.login'))

@auth.route('/login',methods=['POST'])
def login_post():
    name=request.form.get('inputName')
    email=request.form.get('exampleInputEmail1')
    password=request.form.get('exampleInputPassword1')
    print(name,email,password)
    return redirect (url_for('main.profile'))