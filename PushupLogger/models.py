from . import db
## user mixin class from flask-login is a easy way to implement common authentication functionalities
from flask_login import UserMixin

class user(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(100), unique=True)
    password= db.Column(db.String(100))
    name=db.Column(db.String)

    def __repr__(self):
       return '<User %r>' % self.username
    


