from datetime import datetime
from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_name = db.Column(db.String(50))
    plant_description = db.Column(db.String(300))
    is_heirloom = db.Column(db.Boolean)
    price = db.Column(db.Numeric(6,2))
    img_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    modified_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #fk
    category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))
    #fk
    inventory_id = db.Column(db.Integer, db.ForeignKey('product_inventory.id'))
    #fk
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'))
    #backref to order items
    order_items = db.relationship('Order_item', backref='order_items', lazy='dynamic')
    #backref to cart_items
    cart_items = db.relationship('Cart_item', backref='cart_items', lazy='dynamic')

    def __repr__(self):
        return '<Product {}>'.format(self.plant_name) 
    
    def __init__(self, plant_name, plant_description, is_heirloom, price, img_url, category_id, inventory_id=None, seller_id=None):
        self.plant_name = plant_name
        self.plant_description = plant_description
        self.is_heirloom = is_heirloom
        self.price = price
        self.img_url = img_url
        self.category_id = category_id
        self.inventory_id = inventory_id
        self.seller_id = seller_id
        db.session.add(self)
        db.session.commit()


class Product_inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity_available = db.Column(db.Integer)
    #backref
    products = db.relationship('Product', backref='product_by_inventory', lazy='dynamic')

    def __repr__(self):
        return '<Inventory {}>'.format(self.quantity_available) 

    def __init__(self, quantity_available):
        self.quantity_available = quantity_available
        db.session.add(self)
        db.session.commit()

class Product_category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category =  db.Column(db.String(50))
    #backref
    products = db.relationship('Product', backref='product_by_cat', lazy='dynamic')
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    modified_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Category {}>'.format(self.category) 
    
    def __init__(self, category):
        self.category = category
        db.session.add(self)
        db.session.commit()
