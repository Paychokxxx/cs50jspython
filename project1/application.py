from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_session import Session
import os
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from models import Users
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
 
@app.route('/')
def index():
        return "Project 1: TODO"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('success'))
    return render_template('login.html', title='Sign In', form=form)