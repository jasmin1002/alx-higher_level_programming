#!/usr/bin/python3
"""Square Class"""


class Square:
    """Square implements data abstration

    __init__ sets optional default value of size

    Arg:
        size(int): describes the size of a square

    Attribute:
        __size(int): describes the size of a square

    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """int: return the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if int(value) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.size ** 2
