-- This script creates a database hbtn_0d_2
-- and the user user_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'e83e5a17881f.67b91602.alx-cod.online'
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@'e83e5a17881f.67b91602.alx-cod.online';
