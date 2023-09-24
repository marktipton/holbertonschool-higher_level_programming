#!/usr/bin/python3
"""loads object from json file"""
import json


def load_from_json_file(filename):
    """loads object from json file"""
    with open(filename, 'r', encoding='utf-8') as file:
        my_obj = json.loads(file.read())
        return my_obj
