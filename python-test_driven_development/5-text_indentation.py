#!/usr/bin/python3
"""prints text with 2 new lines after '.', '?', and ':'"""


def text_indentation(text):
    """iterates through text string and puts lines at specials chars"""
    for element in text:
        if element == '.' or element == ':' or element == '?':
            print(element)
            print()
        else:
            print(element, end='')
