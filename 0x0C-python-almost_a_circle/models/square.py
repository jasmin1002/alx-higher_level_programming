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
        self.size = size

    @property
    def size(self):
        """Read the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value of width and height attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update modifies class instance's value
        Args:
            args (tuple): no-keyword argument
            kwargs (dictionary): key-worded argument
        """
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                else:
                    self.y = j

        else:
            """kwargs parameter"""
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of square"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic

    def __str__(self):
        """Returns printable text-info for class instance"""
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.size
        )
