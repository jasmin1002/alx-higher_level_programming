#!/usr/bin/python3
'''
    Persist both cities and states tables
    with some data
'''

if __name__ == '__main__':
    import sys

    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    from relationship_city import City
    from relationship_state import Base, State

    inputs = sys.argv[1:]

    # Unpack inputs value
    try:
        username, passwd, db_name = inputs

        # Connection url
        db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
            format(username, passwd, db_name)

        # Create lazy database connection
        engine = create_engine(db_url, pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Establish connection for transaction
        Session = sessionmaker(bind=engine)
        session = Session()

        state = State(name='California')
        city = City(name='San Francisco')
        state.cities.append(city)

        session.add(state)
        session.commit()

        session.close()
    except ValueError:
        msg = "Not enough inputs (expect 3, got {})".format(len(inputs))
        print(msg)

    except Exception as err:
        print("Error: {}".format(err))

    finally:
        # Exit the program unsuccessful
        sys.exit(1)
