#!/usr/bin/python3
"""class base geometry"""


class BaseGeometry:
    """class geometry with method to find area"""
    
    def area(self):
        """gives exception if not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if integer input is greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
