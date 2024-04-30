## LOGIN features
from flask import Blueprint, render_template

## __name__ represents the name of the current file, it ensures Blueprint can find its resources relative to the file
## location
auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template('login.html')
@auth.route('/signup')
def signup():
    return render_template('signup.html')