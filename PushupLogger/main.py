## CRUD operations 
from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user

## Blueprint is logical grouping of flask components
main= Blueprint('main',__name__)

@main.route('/')

def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',name=current_user.name)

@main.route('/logout')
def logout():
    return render_template('logout.html')
