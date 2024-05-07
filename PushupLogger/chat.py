from flask import Blueprint, render_template, url_for, request, redirect, flash

from flask_login import login_required, current_user
from flask_socketio import send
from flask_cors import cross_origin

from . import socketio
chat = Blueprint('chat', __name__)

@cross_origin(origin='*')
@socketio.on('message')
def handleMessage(msg):
    name=current_user.name
    if(msg=='Connected to server'):
        msg=name+" is now "+msg
        # encoded_msg=msg.encode('utf-8')
        print(msg)
        send(msg, broadcast=True)
    else:
        msg=name+":"+msg
        send(msg, broadcast=True)

@login_required
@chat.route('/globalchat')
def globalchat():
    return render_template('globalchat.html')


