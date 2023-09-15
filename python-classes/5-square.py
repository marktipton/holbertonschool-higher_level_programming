#!/usr/bin/python3
"""defines class square"""


class Square:
    """class square with private attribute size"""
    def __init__(self, size=0):
        """Args: size (int): The size of the square."""
        self.__size = size

    @property
    def size(self):
        """gets size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set a new value for size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints square with # in stdout"""
        if self.__size == 0:
            print()
        for i in range (self.__size + 1):
            print("#" * self.__size)
