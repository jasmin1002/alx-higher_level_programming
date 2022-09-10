#!/usr/bin/python3

'''
    Retrieve all data store in states
    table through SQLalchemy syntax
'''

if __name__ == '__main__':
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    from model_state import Base, State

    inputs = sys.argv[1:]

    # Unpack inputs value
    try:
        username, passwd, db_name = inputs
        database_url = "mysql+mysqldb://{}:{}@localhost/{}".format(username, passwd, db_name)

        # Create lazy connection with MySQL via mysqldb
        engine = create_engine(database_url, pool_pre_ping=True)

        print(engine)

        # Create necessary MySQL database table
        # e.g CREATE TABLE table_name
        Base.metadata.create_all(engine)

        # Create a Session
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(State).order_by(State.id).all()

        for state in result:
            print("{}: {}".format(state.id, state.name))

    except ValueError:
        msg = "Not enough inputs (expect 3, got {})".format(len(inputs))
        print(msg)

    except Exception as err:
        print("Error: {}".format(err))

    finally:
        # Exit program with unsuccessful status
        sys.exit(1)
