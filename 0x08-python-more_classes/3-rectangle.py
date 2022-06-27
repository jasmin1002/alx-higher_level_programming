#!/usr/bin/python3
"""Rectangle Module defines a Rectangle class"""


class Rectangle():
    """
    Rectangle class defines two instance varibles width and height

    Instance init method:
        sets the value of instance variable with passed arguments

    Args:
        width: 0 or positive integer
        height: 0 or positive integer

    Attributes:
        width: int
        height: int
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the value of private instance variable width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of private instance variable width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value of private instance variable height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of private instance variable height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of rectangle instance"""
        return self.width * self.height

    def perimeter(self):
        """
        Computes the perimeter of rectangle instance if only
        either width or height is not zero (0).

        0 is returned if either attribute is zero
        """
        if self.width != 0 and self.height != 0:
            return 2 * (self.width + self.height)
        return 0

    def __str__(self):
        """
        Write to stdout the shape of rectange according to its dimension
        with # whenever any instance of rectangle is used with print() or
        str().
        """
        shape = ''

        if self.width == 0 and self.height == 0:
            return shape
        else:
            for i in range(self.height):
                for j in range(self.width):
                    shape += '#'

                    if j == self.width - 1:
                        shape += '\n'
            return shape
