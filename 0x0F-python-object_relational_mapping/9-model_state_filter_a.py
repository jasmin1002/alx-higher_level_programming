#!/usr/bin/python3
'''
    Retain only queryset that contain 'a'
'''

if __name__ == '__main__':
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    from model_state import State, Base

    inputs = sys.argv[1:]

    # Unpack inputs values
    try:
        username, passwd, db_name = inputs

        # Database connection url
        conn_db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, passwd, db_name
        )

        # Create lazy connection
        engine = create_engine(conn_db_url, pool_pre_ping=True)

        # Create any necessary but required database
        # table stated in mapped class (State class)
        Base.metadata.create_all(engine)

        # Establish transaction connection
        Session = sessionmaker(bind=engine)
        session = Session()

        # Retrieve all states that contain 'a'
        # after successful connection
        states = session.query(State).order_by(State.id).all()

        for state in states:
            name = state.__dict__['name']

            if name.find('a') != -1:
                print("{}: {}".format(state.id, name))

        session.close()
    except ValueError:
        # Error message
        msg = "Not enough inputs (expect 3, got {})".format(len(inputs))
        print(msg)

    except Exception as err:
        print("Error: {}".format(err))

    finally:
        # Exit the program unsuccessful
        sys.exit(1)
