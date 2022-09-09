#!/usr/bin/python3

'''
    This script connects to MySQL database using
    MySQLdb module.

    It returns a queryset of state_name filter by
    user's input of name of a state after successful
    connection.
'''

if __name__ == '__main__':
    import sys
    import MySQLdb

    inputs = sys.argv[1:]

    # Unpack input values
    try:
        print(inputs)
        mysql_username, mysql_passwd, db_name, s_name = inputs
    except ValueError:
        msg = "Not enough inputs (expect 3, got {})".format(len(inputs))
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

        # query
        query = "SELECT * FROM states WHERE BINARY name = '{}'\
                ORDER BY id".format(str(s_name))
        cur.execute(query)

        # Retrieve and store the queryset in state variable
        states = cur.fetchall()

        # Print the result to console (stdout)
        for state in states:
            print(state)

        # Close open connection
        cur.close()
        db.close()

    except MySQLdb.Error as err:
        print("MySQL Error: {}".format(err.args[1]))
