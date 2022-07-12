#!/usr/bin/python3
"""Base Class declaration"""


class Base:
    '''
    Base class defines class attribute, nb_objects, which
    keeps track of number of instance of the class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        init method initializes Base's instance attribute

        Args:
            id (int): optional and defaults to None
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
