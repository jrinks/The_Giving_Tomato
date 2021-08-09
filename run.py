from app import create_app, db
from app.blueprints.cart.models import Session_cart, Cart_item
from app.blueprints.user.models import User
from app.blueprints.order.models import Order, Order_item, Order_payment
from app.blueprints.product.models import  Product, Product_inventory, Product_category
from app.blueprints.seller.models import Seller, Pickup, Charity


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Product': Product, 'Product_inventory': Product_inventory, 'Product_category': Product_category, 'Seller': Seller, 'Pickup': Pickup, 'Order': Order, 'Order_item': Order_item, 'Order_payment': Order_payment, 'Session_cart': Session_cart, 'Cart_item': Cart_item}