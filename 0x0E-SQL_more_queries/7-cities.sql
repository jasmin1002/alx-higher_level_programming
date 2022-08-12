-- This script creates a database hbtn_0d_usa and
-- a table cities (in the database hbtn_0d_usa) on
-- MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY(id),
	CONSTRAINT FOREIGN KEY(state_id) REFERENCES states(id)
);
