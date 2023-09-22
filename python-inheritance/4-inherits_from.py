#!/usr/bin/python3
"""returns true obj is instance of a subclass of a class"""


def inherits_from(obj, a_class):
    """checks if obj is instance of subclass of a_class"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
