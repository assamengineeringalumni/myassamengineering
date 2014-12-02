from app import db
from app import app
import flask.ext.whooshalchemy as whooshalchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True,unique=False,)
    branch = db.Column(db.String(64), index=True,unique=False)
    passyear = db.Column(db.String(64), index=True, unique=False)
    hostel = db.Column(db.String, index=True,primary_key=False)
    emailid = db.Column(db.String(64),index=True, unique=True)
    phone=db.Column(db.String(64),index=True,unique=True)
    def __repr__(self):
        return '<User %r>' %(self.username)
        

