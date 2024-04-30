### init.py will be only used once for like setting up database and login features for each instance

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


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
    app.config['SECRET_KEY'] = '12345'

    ##INITIALIZING our database
    db.init_app(app)

    #import after initializing to remove circular dependency error
    from .models import user

    ##login manager is used for session management creation and deletion
    login_manager=LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    ##after the session is created we need to load the user by the user id using userloader
    @login_manager.user_loader
    def load_user(user_id):
        ##load the user by the user id
        return user.query.get(int(user_id))

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app
