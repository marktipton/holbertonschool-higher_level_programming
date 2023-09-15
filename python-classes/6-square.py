#!/usr/bin/python3
"""defines class square"""


class Square:
    """class square with private attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        """Args: size (int): The size of the square."""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """gets position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set a new value for position of square"""
        if isinstance(value, tuple) and value[0] is int and value[1] is int:
            if t[0] > 0 and t[1] > 0:
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """returns current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints square with # in stdout"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end='')
            print("#" * self.__size)
