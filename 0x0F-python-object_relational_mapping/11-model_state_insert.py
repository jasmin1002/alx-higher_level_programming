#!/usr/bin/python3
'''
    Insert new row of state object into
    states table
'''

if __name__ == '__main__':
    import sys

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from model_state import State, Base

    inputs = sys.argv[1:]

    # Unpack input values
    try:
        username, passwd, db_name = inputs

        # Database connection url
        db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
            format(username, passwd, db_name)

        # Create lazy database connection
        engine = create_engine(db_url, pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Establish transaction connection
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create new entry
        louisiana = State(name='Louisiana')
        session.add(louisiana)

        # Commit new entry to repository (Database)
        session.commit()

        session.refresh(louisiana)
        print(louisiana.id)

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
