from datetime import datetime
from app import db
from app.blueprints.user.models import User
from app.blueprints.product.models import Product

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Numeric(6,2))
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    modified_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #fk payment_id
    payment_id = db.Column(db.Integer, db.ForeignKey('order_payment.id'))
    #fk user_id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #backref order_item
    order_item = db.relationship('Order_item', backref= 'order_item_order', lazy='dynamic')

    def __repr__(self):
        return '<Order ID {}>'.format(self.id) 

    def __init__(self, total, payment_id, user_id):
        self.total = total
        self.user_id = user_id
        self.payment_id = payment_id
        db.session.add(self)
        db.session.commit()


class Order_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    modified_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #fk order_id
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    #fk product id
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    
    def __repr__(self):
        return '<Order Item {}>'.format(self.id)

    def __init__(self, total, order_id, product_id):
        self.total = total
        self.order_id = order_id
        self.product = product_id
        db.session.add(self)
        db.session.commit()


class Order_payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_amount = db.Column(db.Numeric(6,2))
    provider = db.Column(db.String(50))
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    modified_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    def __repr__(self):
        return '<Order payment {}>'.format(self.id)
   
    def __init__(self, payment_amount, provider, status):
        self.payment_amount = payment_amount
        self.provider = provider
        self.status = status
        db.session.add(self)
        db.session.commit()
