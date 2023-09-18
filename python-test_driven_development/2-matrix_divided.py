#!/usr/bin/python3
"""
divides every element of a matrix by a specified value
"""


def matrix_divided(matrix, div):
    """Divides elements of matrix by value div"""
    divided_matrix = [[]]
    for row in matrix:
        divided_row = []
        for element in row:
            divided_row.append(element / div)
        divided_matrix.append(divided_row)
    return divided_matrix
