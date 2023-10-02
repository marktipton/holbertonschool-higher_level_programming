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
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string rep of object to a file"""
        filename = f"{cls.__name__}.json"
        json_data = []
        if list_objs is not None:
            for obj in list_objs:
                json_data.append(obj.to_dictionary())

        with open(filename, 'w') as file:
            file.write(cls.to_json_string(json_data))

    @staticmethod
    def from_json_string(json_string):
        """converts json string to Python dictionary"""
        if json_string is None or len(json_string) == 0:
            return []
        dictionary_rep = json.loads(json_string)
        return dictionary_rep

    @classmethod
    def create(cls, **dictionary):
        """create dummy instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(8, 10)
        if cls.__name__ == "Square":
            dummy = cls(8)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instances of class"""
