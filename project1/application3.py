#https://www.youtube.com/watch?v=2dEM-s3mRLE
#https://www.youtube.com/watch?v=q7HVghYjwYo&t=0s
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rauaobzeyukdck:7ea07cfff718faeeb1264bbb340dc2c9cb765f1ea4b49a148d8129c1512cab9e@ec2-54-243-147-162.compute-1.amazonaws.com:5432/d5145tsi8j44qn'
app.config['SECRET_KEY'] = 'thisissecret'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route('/')
def index():
    user = Users.query.filter_by(login='bob',password='bob').first()
    login_user(user)
    return 'You are now logged in!'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are now logged out!'

@app.route('/home')
@login_required
def home():
    return 'The current user is ' + current_user.login 

if __name__ == '__main__':
    app.run(debug=True)