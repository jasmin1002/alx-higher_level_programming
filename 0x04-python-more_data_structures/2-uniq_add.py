#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
    unique digits are added
    '''
    if type(my_list) is not list:
        return
    uniq_list = list(set(my_list))
    total = 0
    for i in range(len(uniq_list)):
        total += uniq_list[i]
    return total
