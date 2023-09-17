#!/usr/bin/python3
"""script that lists one State object from the database """
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], "", sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    x = sys.argv[4]
    s = session.query(State).filter(State.name.like('{}'.format(x))).first()
    if s is not None:
        print("{}".format(s.id))
    else:
        print("Not found")
    session.close()
