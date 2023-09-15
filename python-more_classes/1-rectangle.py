#!/usr/bin/python3
"""Creates a class rectangle"""


class Rectangle:
    """empty class rectangle"""
    def __init__(self, width=0, height=0):
        """defines args width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """gets rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets rectangle width to input value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets rectangle height to input value"""
        if not isinstance (value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
