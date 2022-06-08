#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
        square_matrix_simple returns squares of input matrix
    """
    if type(matrix) is not list:
        return
    if len(matrix[0]) == 0:
        return
    squares = []
    for idx in range(len(matrix)):
        tmp = list(map(lambda x: x**2, matrix[idx]))
        squares.append(tmp)
    return squares
