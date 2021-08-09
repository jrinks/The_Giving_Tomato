from . import bp as user
from app import db
from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user
#from flask_mail import Message
from werkzeug.security import check_password_hash
from .models import User
from .forms import LoginForm, UserInfoForm

@user.route('/')
@user.route('/index')
def index():
    return render_template('index.html', title='Home')

@user.route('/register', methods=['GET', 'POST'])
def register():
    title = 'REGISTER'
    form = UserInfoForm()
    if request.method == 'POST':
        username = form.username.data
        email = form.email.data
        password_hash = form.password_hash.data
        # print(username, email, password)
        # Check if username/email already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).all()
        if existing_user:
            flash('That username or email already exists. Please try again', 'danger')
            return redirect(url_for('auth.register'))
        
        new_user = User(username, email, password_hash)
        db.session.add(new_user)
        db.session.commit()

        flash(f'Thank you {username} for registering!', 'success')

        #msg = Message(f'Thank you, {username}', recipients=[email])
        #msg.body = f'Dear {username}, thank you so much for signing up for this super cool app. I hope you enjoy and also you look super good today!'
        #mail.send(msg)

        return redirect(url_for('main.index'))


    return render_template('register.html', title=title, form=form)


@user.route('/login', methods=['GET', 'POST'])
def login():
    title = 'LOGIN'
    form = LoginForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password_hash.data

        user = User.query.filter_by(username=username).first()
        if user is None or not (user.password_hash == password):
            flash('The Username or Password you entered is incorrect. Please try again.', 'danger')
            return redirect(url_for('user.login'))
        
        login_user(user, remember=form.remember_me.data)
        flash('You have succesfully logged in!', 'success')
        return redirect(url_for('cart.shop'))

    return render_template('login.html', title=title, form=form)


@user.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out!', 'primary')
    return redirect(url_for('user.index'))


