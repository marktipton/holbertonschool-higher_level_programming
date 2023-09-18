#!/usr/bin/python3
"""
divides every element of a matrix by a specified value
"""


def matrix_divided(matrix, div):
    """Divides elements of matrix by value div"""
    divided_matrix = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    for row in matrix:
        divided_row = []
        for element in row:
            if not isinstance(element, (float, int)):
                    raise TypeError(""""
matrix must be a matrix (list of lists) of integers/floats""")
            divided_row.appenid(round(element / div, 2))
        divided_matrix.append(divided_row)
    return divided_matrix
