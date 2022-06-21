#!/usr/bin/python3
"""Square Class"""


class Square:
    """Square controls the type and value of its attribute

    __init__ sets optional default value of size

    Arg:
        size(int): describes the size of a square

    Attribute:
        __size(int): describes the size of a square


    """
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError
            self.__size = int(size)
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
