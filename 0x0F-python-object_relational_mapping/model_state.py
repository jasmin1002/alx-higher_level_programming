#!/usr/bin/python3

'''
    State Model
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    '''
        State maps to a row in states table

        Attributes:
            id (int): A row unique key for entity integrity
            name (string): A name description for a state
    '''

    #: str: Database table maps to.
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
