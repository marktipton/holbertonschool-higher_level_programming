#!/usr/bin/python3
"""prints a square using the '#' character"""


def print_square(size):
    """prints a square using #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print("#" * size)
