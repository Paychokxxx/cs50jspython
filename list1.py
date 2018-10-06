from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    flights = Flight.query.all() #SELECT * FROM flights / flights is list of objects
    for flights in flights:
        print(f"{flights.origin} to {flights.destination}, {flights.duration} minutes.")

if __name__ == "__main__":
    with app.app_context():
        main()