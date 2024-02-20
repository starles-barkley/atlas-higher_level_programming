-- Lists all cities in the database
SELECT cities.id, cities.name, states.name FROM cities
LEFT JOIN states ON cities.state_id = states.id ORDER BY id ASC;
