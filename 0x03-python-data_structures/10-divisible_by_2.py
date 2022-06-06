#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if type(my_list) is not list:
        return
    if len(my_list) == 0:
        return
    new_list = []
    new_list = [num % 2 == 0 for num in my_list]
    return new_list
