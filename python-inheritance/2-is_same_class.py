#!/usr/bin/python3
"""function that returns true if object is an instance of specified class"""


def is_same_class(obj, a_class):
    """returns true if object is exactly and instance of class"""
    if type(obj) == a_class:
        return True
    return False
