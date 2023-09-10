#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    column = len(matrix[0])
    for x in range(row):
        for y in range(column):
            print(matrix[x][y], end=" ")
        print()
