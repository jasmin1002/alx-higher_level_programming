#!/usr/bin/python3
def no_c(my_string):
    if type(my_string) is str:
        new_str = ''
        for char in my_string:
            if chr(ord(char)+32) != 'c' and chr(ord(char)-32) != 'C':
                new_str += char
    return new_str
