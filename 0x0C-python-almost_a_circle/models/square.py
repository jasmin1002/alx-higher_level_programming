#!/usr/bin/python3
"""Square class declaration"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square extends base class, Rectangle

    Args:
        Rectangle (Base): super class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ sets the value of instance variable

        Args:
            size (int): describes both the width and height of a square
            x (int): horizontal distance (x-coordinate)
            y (int): vertical distance (y-coordinate)
            id (int): instance identification number
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """Read the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value of width and height attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns printable text-info for class instance"""
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.size
        )
