#!/usr/bin/python3
'''
    Filter the queryset and select
    a state by user's input choice
'''

if __name__ == '__main__':
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    from model_state import Base, State

    inputs = sys.argv[1:]

    # Unpack inputs value
    try:
        username, passwd, db_name, state = inputs

        # Database connection url
        db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
            format(username, passwd, db_name)

        # Create lazy connection
        engine = create_engine(db_url, pool_pre_ping=True)

        # Create necessary database table
        Base.metadata.create_all(engine)

        # Establish connection for transaction
        Session = sessionmaker(bind=engine)
        session = Session()

        # Filter and retrieve by user input's choice
        states = session.query(State).filter(State.name == state).\
            order_by(State.id).all()

        if len(states) == 0:
            print("Not found")
        else:
            for state in states:
                print(state.id)

        session.close()
    except ValueError:
        # Error message
        msg = "Not enough inputs (expect 4, got {})".\
            format(len(inputs))

        print(msg)
    except Exception as err:
        # Print generic error msg
        print("Error: {}".format(err))

    finally:
        # Exit the program unsuccessful
        sys.exit(1)
