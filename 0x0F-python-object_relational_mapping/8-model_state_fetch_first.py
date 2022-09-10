#!/usr/bin/python3

'''
    Retrieve first row of all
'''

if __name__ == '__main__':
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    from model_state import Base, State

    inputs = sys.argv[1:]

    # Unpack inputs value
    try:
        username, passwd, db_name = inputs

        # Database connection url
        conn_db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, passwd, db_name
        )

        # Create lazy connection
        engine = create_engine(conn_db_url, pool_pre_ping=True)

        # Create appropriate database table required
        # stated in mapped class (State)
        Base.metadata.create_all(engine)

        # Establish transaction connection
        Session = sessionmaker(bind=engine)
        session = Session()

        # Retrieve the first row in a database table
        # after successful connection
        state = session.query(State).first()

        # Print retrieved information
        if state is None:
            print("Nothing\n")
        else:
            print("{}: {}".format(state.id, state.name))

        # Close open connection
        session.close()

    except ValueError:
        msg = "Not enough inputs (expect 3, got {})".format(len(inputs))
        print(msg)
    except Exception as err:
        print("Error: {}".format(err))
    finally:
        # Exit the program unsuccessful
        sys.exit(1)
