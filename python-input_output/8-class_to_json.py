#!/usr/bin/python3
"""returns dictionary description of an object"""


def class_to_json(obj):
    """returns dictionary description of an object"""
    class_name = obj.__class__.__name__
    dictionary_des = {"__class__": class_name}
    attributes = vars(obj)
    for at_name, at_value in attributes.items():
        dictionary_des[at_name] = at_value

    return dictionary_des
