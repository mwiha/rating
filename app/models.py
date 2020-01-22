from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import db, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db,Model,UserMixin):
    id = db.Column(db.Interger , primary_key=True)
    username =db.Column(db.string(20),unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True , nullable=False)
    password =db.Column(db.String(60),nullable=False)
    
    






