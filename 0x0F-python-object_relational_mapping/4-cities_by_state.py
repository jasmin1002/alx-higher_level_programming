#!/usr/bin/python3

'''
    Make connection to MySQL database
    through MySQLdb driver.

    Print to stdout the queryset of cities
    table after successful connection
'''

if __name__ == '__main__':
    import sys
    import MySQLdb

    inputs = sys.argv[1:]

    # Unpack inputs value
    try:
        mysql_username, mysql_passwd, db_name = inputs
    except ValueError:
        msg = "Not enough inputs (expect 3, got {})".format(len(inputs))
        print(msg)

        # Exit the program if No. of inputs < 3
        sys.exit(1)

    try:
        # Create database connection
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_passwd,
            db=db_name
        )

        cur = db.cursor()

        # MySQL Query
        query = "SELECT cities.id, cities.name, states.name FROM \
                cities INNER JOIN states ON states.id = cities.state_id \
                ORDER BY cities.id ASC"
        cur.execute(query)

        # Retrieve and store the queryset
        cities = cur.fetchall()

        for city in cities:
            print(city)

        # Close all open connection
        cur.close()
        db.close()

    except Exception as err:
        # Print exception
        print("Error: {}".format(err))
