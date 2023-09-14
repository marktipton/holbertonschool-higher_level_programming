#!/usr/bin/python3
"""defines class square"""


class Square:
    """class square with private attribute size"""
    def __init__(self, size=0):
        """Args: size (int): The size of the square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
