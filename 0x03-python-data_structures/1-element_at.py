#!/usr/bin/python3
def element_at(my_list=[], idx=0):
    value = None if idx < 0 or idx >= len(my_list) else my_list[idx]
    return value
