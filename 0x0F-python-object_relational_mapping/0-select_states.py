#!/usr/bin/python3
'''
    This script uses MySQLdb module
    to connect to MySQL database and
    query the database for lists of 
    states in states table.
'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    inputs = sys.argv[1:]
    try:
        mysql_username, mysql_passwd, db_name = inputs
    except ValueError:
        print(
            "Not enough inputs (expected 3, got {})".format(len(inputs))
        )
        sys.exit(1)

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_passwd,
            db=db_name
        )

        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        states = cur.fetchall()

        for state in states:
            print(state)

        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e.args[1]))
