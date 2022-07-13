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
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        elif type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
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
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter function: return height's value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function: set the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter function: return x's value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter function: set the value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter function: return y's value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function: set the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """area computes the area of any given rectangle instance"""
        return self.width * self.height

    def display(self):
        """display draws rectangle shape with its dimensions"""
        print('\n' * self.y, end='')
        for row in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """__str__ prints readable text-info describing the
        class instance
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
                self.__class__.__name__,
                self.id,
                self.x,
                self.y,
                self.width,
                self.height
        )
