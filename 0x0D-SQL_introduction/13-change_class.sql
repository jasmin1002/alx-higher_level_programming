-- This script removes all records with a point
-- below 5 or equl 5 in the table second_table of 
-- database hbtn_0c_0 in MySQL.
DELETE FROM second_table WHERE score <= 5;
