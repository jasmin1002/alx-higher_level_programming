#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary={}):
    if type(a_dictionary) is not dict:
        return
    for element in sorted(a_dictionary):
        print("{}: {}".format(element, a_dictionary[element]))
