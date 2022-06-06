#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if type(matrix) is not list:
        return
    if len(matrix[0]) == 0:
        print('')
    else:
        for i in range(len(matrix)):
            idx = 0
            while idx < len(matrix[i]):
                if idx == len(matrix[i]) - 1:
                    print("{:d}".format(matrix[i][idx]))
                    break 
                print("{:d}".format(matrix[i][idx]), end=' ')
                idx += 1
