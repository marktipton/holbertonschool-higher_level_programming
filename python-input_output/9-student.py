#!/usr/bin/python3
"""defines class Student"""


class Student:
    """class student with attr for firstname, lastname, and age"""

    def __init__(self, first_name, last_name, age):
        """initializes public attributes of class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary description of self"""
        dictionary_des = {}
        attr = vars(self)
        for attr_name, attr_value in attr.items():
           dictionary_des[attr_name] = attr_value
        return dictionary_des
