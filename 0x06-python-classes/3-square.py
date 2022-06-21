#!/usr/bin/python3
"""Square Class"""


class Square:
    """
    Square finds the size of its area


    __init__ sets optional default value of size

    Arg:
        size(int): describes size of a square

    Attribute:
        __size(int): describes size of a square

    """
    def __init__(self, size=0):
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        elif type(size) != int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
