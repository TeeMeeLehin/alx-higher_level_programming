#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        r1 = [x**2 for x in row]
        new_matrix.append(r1)
    return new_matrix
