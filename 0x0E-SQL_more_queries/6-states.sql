-- This script creates a database hbtn_0d_usa and
-- a table states (in the databse hbtn_0d_usa) on
-- MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL UNIQUE,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);
ALTER TABLE states MODIFY id INT AUTO_INCREMENT;
