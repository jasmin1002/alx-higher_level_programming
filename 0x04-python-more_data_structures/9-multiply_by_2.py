#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if type(a_dictionary) is not dict:
        return
    new_dict = {x: a_dictionary[x]*2 for x in a_dictionary}
    return new_dict
