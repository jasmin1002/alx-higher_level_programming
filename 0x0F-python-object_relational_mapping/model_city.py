#!/usr/bin/python3
'''
    City Model class description
'''

from sqlachemy import (Column, Integer, String, ForeignKey)
from model_state import Base


class City(Base):
    '''
    A row representation for city entry in cities table


    Args:
        name (str): city name
        state_id (int): reference id to parent table (states)


    Attributes:
        id (int): auto-populate data column
        name (str): Descriptive name data column
        state_id (int): Normalised foreign key column
    '''

    #: list of tuple: cities table
    __tablename__ = 'cities'

    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement='auto',
        unique=True
    )

    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))

    # Relationship
    state = relationship('State')
