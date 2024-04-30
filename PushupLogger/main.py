## CRUD operations 
from flask import Blueprint, render_template

## Blueprint is logical grouping of flask components
main= Blueprint('main',__name__)

@main.route('/')

def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')

@main.route('/logout')
def logout():
    return render_template('logout.html')
