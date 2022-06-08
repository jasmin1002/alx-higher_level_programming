#!/usr/bin/python3
def best_score(a_dictionary={}):
    if type(a_dictionary) is not dict:
        return None
    return max(a_dictionary, key=a_dictionary.get)
