from . import bp as order
from flask import render_template

@order.route('/')
@order.route('/index')
def get_order():
    return render_template('order_confirmation.html')

