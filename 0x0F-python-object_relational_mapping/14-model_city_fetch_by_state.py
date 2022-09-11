#!/usr/bin/python3
'''
    Print all City rows in a database
'''

if __name__ == '__main__':
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    from model_state import Base, State
    from model_city import City

    inputs = sys.argv[1:]

    # Unpack inputs values
    try:
        username, passwd, db_name = inputs

        # Database connection link
        db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
            format(username, passwd, db_name)

        # Create lazy database connection
        engine = create_engine(db_url, pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Establish connection for transaction
        Session = sessionmaker(bind=engine)
        session = Session()

        cities = session.query(City).join(State).\
            filter(State.id == City.state_id).order_by(City.id).\
            all()

        for city in cities:
            output = "{}: ({}) {}".format(city.state.name, city.id, city.name)
            print(output)

        # Close connection
        session.close()
    except ValueError:
        msg = "Not enough inputs (expect 3, got {})".format(len(inputs))
        print(msg)

    except Exception as err:
        print("Error: {}".format(err))

    finally:
        # Exit the program unsuccessful
        sys.exit(1)
