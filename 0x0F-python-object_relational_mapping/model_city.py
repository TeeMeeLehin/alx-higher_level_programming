#!/usr/bin/python3
""" defining a class object to link with ORM """
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ defining the state class """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
