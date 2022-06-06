#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    constant = 0, 0
    tuple_ac = tuple_a + constant
    tuple_bc = tuple_b + constant
    return tuple_ac[0] + tuple_bc[0], tuple_ac[1] + tuple_bc[1]
