from . import bp as product
from app import db
from flask import render_template, redirect, url_for, flash, request
from .forms import ProductInfoForm, DeleteProductForm
from .models import Product
from wtforms.validators import InputRequired

#for users, view available products
@product.route('/')
def index():
    return render_template('shop.html')

#for sellers, view and edit their own products
@product.route('/sellerproducts', methods=['GET', 'POST'])
def add_product():
    title = 'Add Product'
    form = ProductInfoForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            #username = current_user.username
            plant_name = form.plant_name.data
            plant_description = form.plant_description.data
            is_heirloom = form.is_heirloom.data
            price = form.price.data
            img_url = form.img_url.data
            category_id = form.category_id.data
                    
            new_product = Product(plant_name, plant_description, is_heirloom, price, img_url, category_id)
            db.session.add(new_product)
            db.session.commit()

            flash(f' { plant_name } has been added', 'success')

    myproducts = Product.query.all()
        

    return render_template('seller_products.html', myproducts=myproducts, form=form)
   

#for sellers to delete products
@product.route('/delete/<int:id>', methods=['GET','POST'])
# @login_required
def product_delete(id):
    product = Product.query.get_or_404(id)
    #if form.validate_on_submit():
    db.session.delete(product)
    db.session.commit()
    flash(f'{product.plant_name} has been deleted')
    return redirect(url_for('product.add_product'))
    #return redirect(url_for('seller_index.html'))


# #for sellers to edit existing products
# @product.route('/edit/<int:id>', methods=['GET','POST'])
# # @login_required
# def product_edit(id):
#     product = Product.query.get_or_404(id)
#     #if form.validate_on_submit():
    
    
    
    
#     db.session.commit()
#     flash(f'{product.plant_name} has been deleted')
#     return redirect(url_for('product.add_product'))
#     #return redirect(url_for('seller_index.html'))
    


    