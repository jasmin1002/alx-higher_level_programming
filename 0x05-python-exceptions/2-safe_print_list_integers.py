#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            if type(my_list[i]) is not int:
                continue
            count += 1
            print("{:d}".format(my_list[i]), end='')
    except IndexError:
        raise 
    print()
    return count
