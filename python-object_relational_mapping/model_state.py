#!/usr/bin/python3
"""
Lists all cities from database hbtn_0e_4_usa
"""


import SQLAlchemy

engine = create_engine(
                    'mysql://username:password@localhost:3306/database_name'
                )

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
