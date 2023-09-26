#!/usr/bin/python3
"""creates rectangle child class of BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class child of basegeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """unofficial string representation of rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
