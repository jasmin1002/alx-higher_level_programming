#!/usr/bin/python3
"""
0-add_integer defines a add_integer function.
add_integer takes two arguments of type int or float
and returns int sum.
"""


def add_integer(a=None, b=98):
    """
    Accept args of type int or float and return int sum
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
