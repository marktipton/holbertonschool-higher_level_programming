#!/usr/bin/python3
"""returns the JSON representation of an object"""
import json

def to_json_string(my_obj):
    """returns the JSON representation of an object"""
    json_string = json.dumps(my_obj)
    print(json_string)


