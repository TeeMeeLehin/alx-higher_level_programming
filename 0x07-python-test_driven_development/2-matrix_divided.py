#!/usr/bin/python3
"""
Function to divide a Matrix


"""


def matrix_divided(matrix, div):
    """divide a matrix
        matrix - input matrix
        div - the divisor"""
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
        return
    if div == 0:
        raise ZeroDivisionError("division by zero")
        return
    size = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
            break
        new_row = []
        for val in row:
            if type(val) not in [int, float]:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
                break
            new_row.append(round(val / div, 2))
        new_matrix.append(new_row)
    return new_matrix
