#!/usr/bin/python3
"""Rectangle class defines rectangle object with two dimensions"""


class Rectangle():
    """
    init instantiate an object with two parameter

    Args:
        width: int
        height: int

    Attributes:
        width: zero or positive int
        height: zero or positive int
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width property returns the abstracted data: __width"""

        return self.__width

    @width.setter
    def width(self, value):
        """property is a setter propety for the class"""

        # Only positive integer is valid
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height property returns the value of abstracted data: __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of abstracted data: __height

        Only positive integer is supported"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
