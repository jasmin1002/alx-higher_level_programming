#!/usr/bin/python3
'''
    Delete all entry containing
    'a' in their names
'''

if __name__ == '__main__':
    import sys

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from model_state import State, Base

    inputs = sys.argv[1:]

    # Unpack the inputs value
    try:
        username, passwd, db_name = inputs

        # Connection url
        db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
            format(username, passwd, db_name)

        # Create lazy database connection
        engine = create_engine(db_url, pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Establish transaction connection
        Session = sessionmaker(bind=engine)
        session = Session()

        condition = State.name.like('%a%')
        states = session.query(State).filter(condition).all()

        for state in states:
            session.delete(state)
            session.commit()

        session.close()

    except ValueError:
        msg = "Not enough inputs (expect 3, got {})".format(len(inputs))
        print(msg)

    except Exception as err:
        print("Error: {}".format(err))

    finally:
        # Exit program unsuccessful
        sys.exit(1)
