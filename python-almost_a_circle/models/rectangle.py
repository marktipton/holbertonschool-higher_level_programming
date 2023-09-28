#!/usr/bin/python3
"""Creates rectangle class which inherits from base"""


class Rectangle(Base):
    """rectangle class child of base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y