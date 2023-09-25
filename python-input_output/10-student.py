#!/usr/bin/python3
"""defines class Student"""


class Student:
    """class student with attr for firstname, lastname, and age"""

    def __init__(self, first_name, last_name, age):
        """initializes public attributes of class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary description of self"""
        if attrs is None:
            return vars(self)

        dictionary_des = {}
        for attr_name in attrs:
            if hasattr(self, attr_name):
                dictionary_des[attr_name] = getattr(self, attr_name)
        return dictionary_des
