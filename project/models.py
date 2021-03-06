from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
# class Projet(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     budjet = db.Column(db.String(1000))
#     addresses = db.relationship('Address', backref='person', lazy=True)
#     description = db.Column(db.String(10000))