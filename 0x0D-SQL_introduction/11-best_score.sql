-- This script lists all record with score
-- above 10 points in the table second_table
-- of the database htbn_0c_0 in MySQL server.
SELECT score, name FROM second_table
	WHERE score >= 10
	ORDER BY score
	DESC;
