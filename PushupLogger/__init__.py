### init.py will be only used once for like setting up database and login features for each instance

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)

    username = 'root'
    password = 'Gmail123'
    host = 'localhost'
    port = 3306
    database_name = 'pushupdatabase'

    db_uri = 'mysql+mysqlconnector://' + username + ':' + password + '@' + host + ':' + str(port) + '/' + database_name
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    ##INITIALIZING our database
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app
