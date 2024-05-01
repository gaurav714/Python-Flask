## CRUD operations 
import datetime
from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_login import login_required, current_user, logout_user
#from . import db_mongo
from .mongo import Connection

db_mongo=Connection('pushup_db')
## Blueprint is logical grouping of flask components
main= Blueprint('main',__name__)

@main.route('/')

def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    #query = {'email': current_user.email}
    pushupdata=list(db_mongo.userData.find({'email': current_user.email}))
    print(current_user.email)
    for i in pushupdata:
        print(i.get('pushupcount'))
    return render_template('profile.html',pushupdata=pushupdata)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!')
    return redirect(url_for('main.index'))

@main.route('/addworkout')
@login_required
def addworkout():
    return render_template('addworkout.html')

@main.route('/addworkout', methods=['POST'])
@login_required
def addworkout_post():
    email=current_user.email
    pushupcount=request.form.get('pushupcount')
    comment=request.form.get('comments')
    content={'email':email,'pushupcount':pushupcount,'comments':comment, 'date':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    save=db_mongo.userData.insert_one(content)
    if not save.inserted_id:
        print('Failed to save data')
    else:
        print('Data saved successfully')
        flash('Workout added successfully')
    return redirect(url_for('main.addworkout'))

    

