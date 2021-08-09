from typing import ItemsView
from . import bp as cart
from app import db
from flask import render_template, redirect, url_for, flash, request
from ..product.models import Product
from .models import Cart_item, Session_cart
#for users, view available products



@cart.route('/checkout')
def checkout():
   
    return render_template('checkout.html')



@cart.route('/shop', methods=['GET', 'POST'])
def shop():
    title = 'Add Product To Cart'
    #plant_name = Product.query.get_or_404(id).with_entities(Product.prodocut_name
    cartproducts= Cart_item.query.all()
    myproducts= Product.query.all()

    return render_template('shop.html', cartproducts=cartproducts, myproducts=myproducts)


@cart.route('/add/<int:id>')
def add(id):
    title = 'Add Product To Cart'
    try:
        item = session.query(Cart_item).filter(Cart_item.product_id == id)
        item.quantity = item.quantity +1
        update_item = Cart_item(item)
        db.session.commit()
        flash(f'Item quantity has been updated', 'success')      

    except:
        product_id = id
        quantity = 1
        add_product = Cart_item(quantity, product_id)
        db.session.add(add_product)
        db.session.commit()
    flash(f' An item has been added to your cart', 'success')      
    cartproducts= Cart_item.query.all()
    myproducts= Product.query.all()
    

    return render_template('shop.html', cartproducts=cartproducts, myproducts=myproducts)
    



#for users to delete items from their cart
@cart.route('/delete/<int:id>', methods=['GET','POST'])
# @login_required
def remove_from_cart(id):
    product = Cart_item.query.get_or_404(id)
#     if product.seller.or.id != current_user.id:
#         flash("You cannot delete another user's post. Who do you think you are?", "warning")
#         return redirect(url_for('blog.myposts'))
    #if form.validate_on_submit():
    try:
        db.session.delete(product)
        db.session.commit()
        flash(f'A product has been deleted from your cart')
        return redirect(url_for('cart.shop'))
    except:
        flash(f'A product has been deleted from your cart')
        return redirect(url_for('cart.shop'))
    #return redirect(url_for('seller_index.html'))
