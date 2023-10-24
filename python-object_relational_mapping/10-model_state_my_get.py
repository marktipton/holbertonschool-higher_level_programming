#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states(username, password, database_name, state_searched):
    """list states in hbtn_0e_0_usa database"""
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database_name}'
    )

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State)\
                    .filter(State.name == state_searched)\
                    .first()

    if state:
        print(state.id)
    else:
        print("Not Found")

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_searched = sys.argv[4]
    list_states(username, password, database_name, state_searched)
