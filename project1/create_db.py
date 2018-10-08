from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rauaobzeyukdck:7ea07cfff718faeeb1264bbb340dc2c9cb765f1ea4b49a148d8129c1512cab9e@ec2-54-243-147-162.compute-1.amazonaws.com:5432/d5145tsi8j44qn"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()