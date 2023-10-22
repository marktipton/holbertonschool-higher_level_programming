-- lists all the cities of California that can be found in the database hbtn_0d_usa
USE hbtn_0d_usa;
SET @California_id = (SELECT id FROM states WHERE name = 'California');

SELECT cities.* FROM cities
WHERE state_id = @California_id
ORDER BY cities.id;