#!/usr/bin/python3
"""prints list in ascending order"""


class MyList(list):
    """child class MyList with parent list"""
    def __init__(self):
        super().__init__()


    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
