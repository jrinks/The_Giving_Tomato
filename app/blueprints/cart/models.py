from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.blueprints.order.models import Order, Order_payment, Order_item
from app.blueprints.user.models import User
from app.blueprints.product.models import Product, Product_inventory, Product_category
import os



class Session_cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Numeric(6,2))
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    modified_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #fk user+id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #backref cart_item
    cart_item = db.relationship('Cart_item', backref= 'cart_item_session', lazy='dynamic')

    def __repr__(self):
        return '<Session Card {}>'.format(self.id) 

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)

    def __init__(self, total, user_id):
        self.total = total
        self.user_id = user_id
        db.session.add(self)
        db.session.commit()


class Cart_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    modified_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #fk session_cart_id
    order_id = db.Column(db.Integer, db.ForeignKey('session_cart.id'))
    #fk product id
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    
    def __repr__(self):
        return '<Cart Item {}>'.format(self.id)

    def __init__(self, quantity, product_id):
        self.quantity = quantity
        self.product_id = product_id
        db.session.add(self)
        db.session.commit()
