#!/usr/bin/python3
"""returns pascals triangle using a list of lists"""


def pascal_triangle(n):
    """returns pascals triangle using a list of lists"""
    lol = []
    if n <= 0:
        return lol
    lol = [[1] for x in range(n)]

    for x in range(1, n):
        for y in range(1, x):
            lol[x].append(lol[x - 1][y - 1] + lol[x - 1][y])
        lol[x].append(1)

    return lol
