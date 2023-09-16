#!/usr/bin/python3
"""Creates a class rectangle"""


class Rectangle:
    """rectangle with width and height"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """defines args width and height"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets rectangle width to input value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets rectangle height to input value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimiter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns the rectangle as a string"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            string += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """returns a string recreation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints message when an instance of rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

