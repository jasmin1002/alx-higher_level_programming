#!/usr/bin/python3
"""Rectangle Class Declaration"""


from models.base import Base

class Rectangle(Base):
    """
    Rectangle extends super-class (Base)

    Args:
        Base (Base): super class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init initializes the Rectangle's instance attributes

        Args:
            width (int): width dimension
            height (int): height dimension
            x (int): ...
            y (int): ...
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter function: return width's value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function: set the value of width"""
        self.__width = value

    @property
    def height(self):
        """Getter function: return height's value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function: set the value of height"""
        self.__height = value

    @property
    def x(self):
        """Getter function: return x's value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter function: set the value of x"""
        self.__x = value

    @property
    def y(self):
        """Getter function: return y's value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function: set the value of y"""
        self.__y = value
