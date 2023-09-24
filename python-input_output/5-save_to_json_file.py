#!/usr/bin/python3
"""writes json represenation of object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes json representation of object to a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        json_str = json.dump(my_obj, file)
        return json_str
