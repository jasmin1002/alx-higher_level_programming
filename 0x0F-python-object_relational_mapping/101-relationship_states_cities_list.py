#!/usr/bin/python3
'''
    List all states together with their
    corresponding cities
'''

if __name__ == '__main__':
    import sys

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from relationship_state import Base, State
    from relationship_city import City

    inputs = sys.argv[1:]

    # Unpack inputs values
    try:
        username, passwd, db_name = inputs

        # Database connection url
        db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
            format(username, passwd, db_name)

        # Create lazy connection
        engine = create_engine(db_url, pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Establish transaction connection
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).join(City).\
            order_by(State.id, City.id).all()

        # Print each state row in states collection
        for state in states:
            print("{}: {}".format(state.id, state.name))

            # Print each city attached to each state in
            # cities collection
            for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))

        # Close connection
        session.close()
    except ValueError:
        msg = "Not enough inputs (expect 3, got {})".format(len(inputs))
        print(msg)

    except Exception as err:
        print("Error: {}".format(err))

    finally:
        # Exit the program unsuccessul
        sys.exit(1)
