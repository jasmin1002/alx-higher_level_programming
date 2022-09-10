#!/usr/bin/python3
'''
    Update a states row with new value
'''

if __name__ == '__main__':
    import sys

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from model_state import Base, State

    inputs = sys.argv[1:]

    # Unpack inputs value
    try:
        username, passwd, db_name = inputs

        # Database connection url
        db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
            format(username, passwd, db_name)

        # Create lazy connection
        engine = create_engine(db_url, pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Establish connection for transaction
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter(State.id == 2).\
            first()

        # Update state name
        state.name = 'New Mexico'
        session.add(state)
        session.commit()

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
