from flask import Flask, render_template, url_for, flash, redirect, request
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash,check_password_hash
from users.forms import LoginForm, RegisterForm
import pugsql
import sqlite3
import os



app = Flask(__name__)

queries = pugsql.module('queries/')
queries.connect('sqlite:///lifelog.db')

app.config['SECRET_KEY'] = 'mysecret'

app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = queries.check_username(form.username.data)

        if check_password_hash(user.password, form.password.data) and user is not None:
            login_user(user)
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('index.html')

            return redirect(next)

    return render_template('login.html', form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index.html'))

app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        #check if user exists
        user = queries.check_username(username=form.username.data)

        if user is not None:
            queries.create_user(username=form.username.data, password=generate_password_hash(form.password.data))
            flash('Thanks for registering! Now you can login!')
            return redirect(url_for('login.html'))

        flash('That user already exists')

    return render_template('register.html', form=form)


login_manager = LoginManager()

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "users.login"
