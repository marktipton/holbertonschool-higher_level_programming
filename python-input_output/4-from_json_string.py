#!/usr/bin/python3
"""converts from json to object"""
import json


def from_json_string(my_str):
    """converts from json to object"""
    my_obj = json.loads(my_str)
    return my_obj
