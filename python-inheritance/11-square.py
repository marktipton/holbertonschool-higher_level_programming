#!/usr/bin/python3
"""creates rectangle child class of BaseGeometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """rectangle class child of basegeometry"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """unofficial string representation of square"""
        return f"[Square] {self.__width}/{self.__height}"

