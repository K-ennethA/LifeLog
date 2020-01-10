from flask import Flask, render_template, url_for, flash, redirect, request
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash,check_password_hash

from LifeLog.users.forms import LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

app.route('/login'):
def login():
    form = LoginForm()

    if form.validate_on_submit():




login_manager = LoginManager()

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "users.login"
