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
    new = State(name='Louisiana')
    session.add(new)
    session.commit()
    s = session.query(State).filter(State.name.like('Louisiana')).first()
    print("{}".format(s.id))
    session.close()
