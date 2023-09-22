#!/usr/bin/python3
"""creates rectangle child class of BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__heiht = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
