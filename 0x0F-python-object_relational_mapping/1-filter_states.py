#!/usr/bin/python3

'''
    This script connects to MySQL database
    using MySQLdb module.

    It returns a queryset of states name with
    capital letter N initial after successful
    connection.
'''

if __name__ == '__main__':
    import sys
    import MySQLdb

    inputs = sys.argv[1:]

    # Unpack input values
    try:
        mysql_username, mysql_passwd, db_name = inputs
    except ValueError:
        msg = "Not enough inputs (except 3, got {})".format(len(inputs))
        print(msg)

        # Exit the program if No. of inputs < 3
        sys.exit(1)

    try:
        # Create connection to MySQL database
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_passwd,
            db=db_name
        )

        # Create a cursor to execute a query
        cur = db.cursor()
        cur.execute(
            "SELECT * FROM states WHERE SUBSTR(name, 1, 1) = 'N'\
                ORDER BY id ASC"
        )

        # Retrieve and store the queryset in states variable
        states = cur.fetchall()

        # Print each entity (state) to stdout
        for state in states:
            print(state)

        # Close open connection
        cur.close()
        db.close()

    except MySQLdb.Error as err:
        print("MySQL Error: {}".format(err.args[1]))


