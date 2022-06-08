#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
        square_matrix_simple returns squares of input matrix
    """
    if type(matrix) is not list:
        return
    squares = []
    for idx in range(len(matrix)):
        tmp = list(map(lambda x: x**2, matrix[idx]))
        squares.append(tmp)
    return squares
