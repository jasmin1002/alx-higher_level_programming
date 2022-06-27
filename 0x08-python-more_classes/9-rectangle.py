#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle:
    """Define a Rectangle class with width and height"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle instace attributes
        Args:
            width (int, optional): set integer. Defaults to 0.
            height (int, optional): set integer. Defaults to 0.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width value
        Returns:
            int: width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set width value
        Args:
            value (int): integer
        Raises:
            TypeError: when value is not int
            ValueError: when value is a negative integer
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get height value
        Returns:
            int: height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set height value
        Args:
            value (int): integer
        Raises:
            TypeError: when value is not int
            ValueError: when value is a negative integer
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangle area
        Returns:
            int: Rectangle area
        """
        return self.height * self.width

    def perimeter(self):
        """Rectangle perimeter
        Returns:
            int: Rectangle perimeter
        """
        if self.height is 0 or self.width is 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """String Rectangle form with # character
        Returns:
            str: rectangle with "#"
        """
        hash_print = ""
        if self.width is 0 or self.width is 0:
            return hash_print
        else:
            for i in range(self.height):
                if i + 1 < self.height:
                    hash_print += str(self.print_symbol) * self.width + "\n"
                else:
                    hash_print += str(self.print_symbol) * self.width
        return hash_print

    def __repr__(self):
        """String representation of Rectangle
        Returns:
            str: Representation of the Rectangle class
        """
        return "Rectangle(" + str(self.width) + "," + str(self.height) + ")"

    def __del__(self):
        """Delete base class part of the instance
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method to define a rectangle bigger or equal to other rect
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method to convert rectangle to square
        """
        return cls(size, size)
