SELECT * FROM flights;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE destination = 'Paris';
SELECT * FROM flights WHERE destination = 'Paris' OR duration > 500;

SELECT * FROM flights WHERE destination = 'Paris' AND duration > 500;


SELECT AVG(duration) FROM fligths; -- returns avarage value of duration from all flights
SELECT AVG(duration) FROM fligths WHERE origin = 'New York';  -- returns avarage value of duration from flights originated from New York

SELECT COUNT(*) FROM flights; -- returns number of rows
SELECT COUNT(*) FROM flights WHERE origin = 'New York'; -- returns number of rows

SELECT MIN(duration) FROM flights;
SELECT * FROM flights WHERE duration = 245;

SELECT * FROM flights WHERE origin IN ('New York', 'Lima'); -- range of possible values - OR
SELECT * FROM flights WHERE origin LIKE '%a%'; --search by part of word origin 'a', %-any text

--FUNCTIONs SUM COUNT MIN MAX AVG .....

--LIMIT or TOP()
SELECT * FROM flights LIMIT 2;  --mysql variant
SELECT  TOP(2) * FROM flights; --mssql variant


--ORDER BY
SELECT * FROM flights ORDER BY duration DESC;
-- sort all by DESC
SELECT * FROM flights ORDER BY duration ASC LIMIT 3;  --mysql variant

--GROUP BY
SELECT origin, COUNT(*) FROM flights GROUP BY origin; -- select by groups
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1; -- select by groups only flights with origin city > 1





