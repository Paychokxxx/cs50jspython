--postgress 9.3`

CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL,
    flight_id INTEGER NOT NULL
);

INSERT INTO flights (origin, destination, duration, flight_id) VALUES ('Shanghai', 'Paris', 760, 1);
INSERT INTO flights (origin, destination, duration, flight_id) VALUES ('Istanbul', 'Tokyo', 700, 2);
INSERT INTO flights (origin, destination, duration, flight_id) VALUES ('New York', 'Paris', 435, 3);
INSERT INTO flights (origin, destination, duration, flight_id) VALUES ('Moscow', 'Paris', 245, 4);
INSERT INTO flights (origin, destination, duration, flight_id) VALUES ('Lima', 'Paris', 199, 5);
INSERT INTO flights (origin, destination, duration, flight_id) VALUES ('Lima', 'Shanghai', 250, 6);

CREATE TABLE passengers (
    id SERIAL PRIMARY KEY, 
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
);

INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Ben', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Jack', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Sarah', 4);
INSERT INTO passengers (name, flight_id) VALUES ('John', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Alex', 6);



SELECT * FROM passengers WHERE name = 'Alice';
SELECT * FROM flights WHERE id = 1;

SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flight_id;  --inner join
SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flight.id WHERE name = 'Alice';

SELECT origin, destination, name FROM flights LEFT JOIN passengers ON passengers.flight_id = flight_id; --LEFT join
--RIGHT  join


--CREATE INDEX

-- SELECT + nested sql queries

SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1; -- select flight_id only if it has more than 1 passenger on it

SELECT * FROM flights WHERE id IN 
(SELECT flight_id FROM passengers 
GROUP BY flight_id HAVING COUNT(*) > 1); -- select flight_id only if it has more than 1 passenger on it