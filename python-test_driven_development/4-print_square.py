#!/usr/bin/python3
"""prints a square using the '#' character"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must
    for i in range(size):
        print("#" * size)
