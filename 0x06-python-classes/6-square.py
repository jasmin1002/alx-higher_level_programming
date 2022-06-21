#!/usr/bin/python3
"""Square Class"""


class Square:
    """Square implements data abstration

    __init__ sets optional default value of size and position

    Args:
        size (int): describes the size of a square
        position (tuple): describes the coordinate of a square

    Attributes:
        __size (int): describes the size of a square
        __position (tuple): describes the coordinate of a square

    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: returns size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """tuple: returns coordinate of a square (x, y)"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """int: returns area of a square"""
        return self.size ** 2

    def my_print(self):
        """str: print a character #"""
        if self.size == 0:
            print()
            return
        if self.__position[1] > 0:
            print("\n" * self.position[1], end="")
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
