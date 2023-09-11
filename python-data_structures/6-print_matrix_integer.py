#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    column = len(matrix[0])
    for x in range(row):
        for y in range(column):
            if y == column - 1:
                end_char = ''
            else:
                end_char = ' '
            print("{:d}".format(matrix[x][y]), end=end_char)
        print()
