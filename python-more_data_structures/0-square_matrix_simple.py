#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = list(map(lambda x: [i**2 for i in x], matrix))
    return square_matrix
