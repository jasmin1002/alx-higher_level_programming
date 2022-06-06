#!/usr/bin/python3
def max_integer(my_list=[]):
    if type(my_list) is not list:
        return
    if len(my_list) == 0:
        return None
    temp = my_list[0] 
    for idx in range(1, len(my_list)):
        if my_list[idx] >= temp:
            temp = my_list[idx]
    return temp
