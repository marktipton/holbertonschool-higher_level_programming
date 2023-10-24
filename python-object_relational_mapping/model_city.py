#!/usr/bin/python3
"""
connect to database using sqlalchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy.orm import relationship
Base = declarative_base()


class City(Base):
    """Inherits from Base connects to Mysql"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
    state = relationship("State")
