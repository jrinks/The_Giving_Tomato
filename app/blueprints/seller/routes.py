from . import bp as seller
from app import db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
#from flask_mail import Message
from werkzeug.security import check_password_hash
from ..user.models import User
from .models import Seller, Charity, Pickup
from ..user.forms import LoginForm
from .forms import CharityInfoForm, PickupInfoForm, SellerInfoForm

@seller.route('/')
@seller.route('/index')
def index():
    title = 'SELLERLOGIN'
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user is None or not check_password_hash(user.password_hash, password):
            flash('The Username or Password you entered is incorrect. Please try again.', 'danger')
            return redirect(url_for('seller.login'))
        
        login_user(user, remember=form.remember_me.data)
        flash('You have succesfully logged in to the Sellers portal!', 'success')
        return redirect(url_for('seller.index'))

    return render_template('seller_index.html', title=title, form=form)

@seller.route('/register', methods=['GET', 'POST'])
def register():
    title = 'SELLER REGISTER'
    form = SellerInfoForm()
    if request.method == 'POST' :
    #and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password_hash.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone = form.phone.data
        # print(username, email, password)
        # Check if username/email already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).all()
        if existing_user:
            flash('That username or email already exists. Please try again', 'danger')
            return redirect(url_for('seller.register'))
        

        new_user = User(username, email, password, first_name, last_name, phone, role='seller')
        db.session.add(new_user)
        db.session.commit()

        flash(f'Thank you {username} for registering to be a seller!', 'success')

        #msg = Message(f'Thank you, {username}', recipients=[email])
        #msg.body = f'Dear {username}, thank you so much for signing up for this super cool app. I hope you enjoy and also you look super good today!'
        #mail.send(msg)

        return redirect(url_for('seller.index'))
    return render_template('seller_register.html', title=title, form=form)


@seller.route('/login', methods=['GET', 'POST'])
def login():
    title = 'SELLERLOGIN'
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user is None or not check_password_hash(user.password_hash, password):
            flash('The Username or Password you entered is incorrect. Please try again.', 'danger')
            return redirect(url_for('seller.login'))
        
        login_user(user, remember=form.remember_me.data)
        flash('You have succesfully logged in to the Sellers portal!', 'success')
        return redirect(url_for('seller.index'))

    return render_template('seller_login.html', title=title, form=form)


@seller.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out!', 'primary')
    return redirect(url_for('seller_index.html'))


@seller.route('/pickup', methods=['GET','POST'])
def add_pickupinfo():
    title = 'Add Pickup Info'
    form = PickupInfoForm()
    if request.method == 'POST':
        # and form.validate_on_submit():
        #username = current_user.username
        pickup_date = form.pickup_date.data
        pickup_time = form.pickup_time.data
        pickup_address = form.pickup_address.data
        pickup_city = form.pickup_city.data
        pickup_state = form.pickup_state.data
        pickup_instructions = form.pickup_instructions.data
        
        new_pickup = Pickup(pickup_date, pickup_time, pickup_address, pickup_city, pickup_state, pickup_instructions)
        db.session.add(new_pickup)
        db.session.commit()

        flash(f'you have added a new pickup option', 'success')

        #msg = Message(f'Thank you, {username}', recipients=[email])
        #msg.body = f'Dear {username}, thank you so much for signing up for this super cool app. I hope you enjoy and also you look super good today!'
        #mail.send(msg)

        return redirect(url_for('seller.index'))


    return render_template('seller_pickup.html', title=title, form=form)

@seller.route('/getpickups', methods=['GET'])
def get_pickups():
    title = 'Get Pickup Info'
    mypickups= Pickup.query.all()
 
    return render_template('seller_getpickups.html', mypickups=mypickups)


@seller.route('/charity', methods=['GET', 'POST'])
def add_charityinfo():
    title = 'Add Charity Info'
    form = CharityInfoForm()
    if request.method == 'POST':
        # and form.validate_on_submit():
        #username = current_user.username
        org_name = form.org_name.data
        org_mission = form.org_mission.data
        org_description = form.org_description.data
        org_city = form.org_city.data
        org_state = form.org_state.data
        org_url = form.org_url.data
        
        new_charity = Charity(org_name, org_mission, org_description, org_city, org_state, org_url)
        db.session.add(new_charity)
        db.session.commit()

        flash(f'you have added a new charity option', 'success')

        #msg = Message(f'Thank you, {username}', recipients=[email])
        #msg.body = f'Dear {username}, thank you so much for signing up for this super cool app. I hope you enjoy and also you look super good today!'
        #mail.send(msg)

        return redirect(url_for('seller.index'))


    flash(f'Last return statement reached', 'success')
    return render_template('seller_charity.html', title=title, form=form)

@seller.route('/getcharities', methods=['GET'])
def get_charity():
    title = 'Get Charities Info'
    mycharities= Charity.query.all()
    return render_template('seller_getcharities.html', mycharities = mycharities)


@seller.route('/charities', methods=['GET'])
def charities():
    title = 'Charities We'
    mycharities= Charity.query.all()
    return render_template('charities.html', mycharities = mycharities)
