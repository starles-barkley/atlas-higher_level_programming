-- Create database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
CREATE TABLE IF NOT EXISTS hbtn_0d_states (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
)
