#!/usr/bin/python3

'''
    Creates MySQL database connection through
    MySQLdb module

    And returns filtered the queryset by user's
    input: (state's name) after successful connection.
'''

if __name__ == '__main__':
    import sys
    import MySQLdb

    inputs = sys.argv[1:]

    # Unpack inputs value
    try:
        mysql_username, mysql_passwd, db_name, state = inputs

    except ValueError:
        msg = "Not enough inputs (expect 3, got {}".format(len(inputs))
        print(msg)

        # Exit the program if No. of inputs < 3
        sys.exit(1)

    try:
        # Create MySQL database connection
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_passwd,
            db=db_name
        )

        # Create a cursor to execute a query
        cur = db.cursor()

        # MySQL query
        query = "SELECT cities.name FROM cities INNER JOIN \
                states ON states.id = cities.state_id WHERE \
                states.name = %(name)s ORDER BY cities.id ASC"

        cur.execute(query, {'name': state})

        # Retrieve and store the queryset
        city_table = cur.fetchall()

        # Collate the queryset into flat list
        tmp = tuple(city for row in city_table for city in row)

        # Concatenate the value of list in tmp by ', '
        cities = ', '.join(tmp)

        print(cities)

        # close all open connection
        cur.close()
        db.close()

    except Exception as err:
        # Print exception
        print("Error: {}".format(err))
