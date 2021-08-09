from datetime import datetime
from app import db
from flask_login import UserMixin
from app import login
import os


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    modified_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    role = db.Column(db.String(20))
    #backref
    order = db.relationship('Order', backref='order', lazy='dynamic')
    #backref
    session_cart = db.relationship('Session_cart', backref='session_cart', lazy='dynamic')
    #backref
    seller_id = db.relationship('Seller', backref='seller_id', lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.username) 

    def __init__(self, username, email, password_hash, first_name='', last_name='', phone='', role='user'):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.role = role
        db.session.add(self)
        db.session.commit()

