#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
     The list comprehension yields same result:
     square = [list(map(lambda x: x**2, matrix[idx])) for idx in range(len(matrix))]
        return square
    """
    if type(matrix) is not list:
        return None
    if len(matrix[0]) == 0:
        return None
    squares = []
    for idx in range(len(matrix)):
        tmp = list(map(lambda x: x**2, matrix[idx]))
        squares.append(tmp)
    return squares
