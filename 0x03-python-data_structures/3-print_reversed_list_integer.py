#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for digit in my_list:
        print("{:d}".format(digit))
