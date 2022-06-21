#!/usr/bin/python3
"""Square Class"""


class Square:
    """Square defines a square plane object by size

    The __init__ sets default value of size


    Args:
        size(int): describes size of a square

    Attribute:
        size(int): descibes size of a square

    """

    def __init__(self, size=0):
        self.__size = size
