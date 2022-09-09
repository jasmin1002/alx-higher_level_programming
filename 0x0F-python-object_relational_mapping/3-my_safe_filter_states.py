#!/usr/bin/python3

'''
    This script connects to MySQL database
    using MySQLdb module.

    It returns a queryset for states entity
    after successful connection while preventing
    SQL injection.
'''

if __name__ == '__main__':
    import sys
    import MySQLdb

    inputs = sys.argv[1:]

    # Unpack input values
    try:
        mysql_username, mysql_passwd, db_name, state = inputs
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

        # Query: preventive SQL injection
        query = "SELECT * FROM states WHERE name = %(name)s"
        cur.execute(query, {'name': state})

        # Retrieve all queryset
        states = cur.fetchall()

        for state in states:
            print(state)

        # Close connection
        cur.close()
        db.close()

    except MySQLdb.Error as err:
        print("MySQL Error: {}".format(err.args[1]))
    except Exception as e:
        print("Error: {}".format(e))
