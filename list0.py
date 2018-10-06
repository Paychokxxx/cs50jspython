import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:postgres@localhost:5432/flights")
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flights in flights:
        print(f"{flights.origin} to {flights.destination}, {flights.duration} minutes.")

if __name__ == "__main__":
    main()