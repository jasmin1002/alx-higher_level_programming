#!/usr/bin/python3

'''
    State Model
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    '''
        State maps to a row in states table

        Attributes:
            name (string): A name description for a state

        Args:
            id (int): A row unique auto populate (entity integrity)
    '''

    #: list of tuple: (state): states table maps to.
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)

    # Relationship
    cities = relationship(
        'City',
        back_populates='state',
        cascade='all, delete, delete-orphan'
    )
