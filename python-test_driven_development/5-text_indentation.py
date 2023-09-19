#!/usr/bin/python3
"""prints text with 2 new lines after '.', '?', and ':'"""


def text_indentation(text):
    """iterates through text string and puts lines at specials chars"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    space_flag = 'x'
    for element in text:
        if space_flag == 'x':
            if element == " ":
                continue
            else:
                print(element, end='')
                space_flag = 'y'
        else:
            if element == '.' or element == ':' or element == '?':
                print(f"{element}", end='\n\n')
                space_flag = 'x'
            else:
                print(f"{element}", end='')
