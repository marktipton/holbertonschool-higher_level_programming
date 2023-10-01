#!/usr/bin/python3
"""Manages id attribute for subclasses"""

import json

class Base:
    """Parent class for shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method to list dictionary rep of objects"""
        if list_dictionaries is None:
            return "[]"
        return json.dump(list_dictionaries)
