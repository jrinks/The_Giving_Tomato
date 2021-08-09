from app.blueprints.user.models import User
from datetime import datetime
from app import db

from flask_login import UserMixin

class Charity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    org_name = db.Column(db.String(50))
    org_mission = db.Column(db.String(300))
    org_description = db.Column(db.String(300))
    org_city = db.Column(db.String(50))
    org_state = db.Column(db.String(2))
    org_url = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    modified_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #backref
    seller = db.relationship('Seller', backref= 'seller_charity', lazy='dynamic')

    def __repr__(self):
        return '<Charity {}>'.format(self.org_name) 

    def __init__(self, org_name, org_mission, org_description, org_city, org_state, org_url):
        self.org_name = org_name
        self.org_mission = org_mission
        self.org_description = org_description
        self.org_city = org_city
        self.org_state = org_state
        self.org_url = org_url
        db.session.add(self)
        db.session.commit()


class Pickup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pickup_date = db.Column(db.Date)
    pickup_time = db.Column(db.Time)
    pickup_address = db.Column(db.String(100))
    pickup_city = db.Column(db.String(50))
    pickup_state = db.Column(db.String(2))
    pickup_instructions = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    modified_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #backref
    seller = db.relationship('Seller', backref= 'seller_pickup', lazy='dynamic')

    def __repr__(self):
        return '<Pickup Date {}>'.format(self.pickup_date) 
    
    def __init__(self, pickup_date, pickup_time, pickup_address, pickup_city, pickup_state, pickup_instructions):
        self.pickup_date = pickup_date
        self.pickup_time = pickup_time
        self.pickup_address = pickup_address
        self.pickup_city = pickup_city
        self.pickup_state = pickup_state
        self.pickup_instructions = pickup_instructions
        db.session.add(self)
        db.session.commit()

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    modified_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #fk
    charity_id = db.Column(db.Integer, db.ForeignKey('charity.id'))
    #fk
    pickup_id = db.Column(db.Integer, db.ForeignKey('pickup.id'))
    #fk
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #backref
    product = db.relationship('Product', backref='product_seller', lazy='dynamic')
    

    def __repr__(self):
        return '<User {}>'.format(self.username) 

    def __init__(self, user_id, company_name=None, charity_id=None, pickup_id=None):
        self.user_id = user_id
        self.company_name = company_name
        self.charity_id = charity_id
        self.pickup_id = pickup_id
        db.session.add(self)
        db.session.commit()

