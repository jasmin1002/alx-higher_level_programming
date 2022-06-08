#!/usr/bin/python3
def search_replace(my_list=[], search="", replace=""):
    '''
    Search_replace function replaces
    all occurrences of an element by
    given replaced value parameter
    '''
    if type(my_list) is not list:
        return
    new_list = []
    size = len(my_list)
    for i in range(size):
        value = my_list[i] if my_list[i] != search else replace
        new_list.append(value)
    return new_list
