#!/usr/bin/python3
"""Rectangle includes area and perimeter attributes to class definition"""


class Rectangle():
    """
    Creates instance of Rectangle class with attrs:

    Attributes:
        width: 0 or positive integer
        height: 0 or positive integer

    Instance init:
        initializes instance attributes with the given arguments:
        Args:
            width: positive int
            height: positive int
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the value of private data: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of private data: width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the value of private data: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of private data: height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes the area of rectangle instance"""
        return self.width * self.height

    def perimeter(self):
        """Computes the perimeter of rectangle instance"""
        if self.width != 0 and self.height != 0:
            return 2 * (self.width + self.height)
        return 0
