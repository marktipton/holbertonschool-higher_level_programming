#!/usr/bin/python3
"""writes a string to a utf8 text file"""


def write_file(filename="", text=""):
    """writes string to text file"""
    with open(filename, 'w', encoding = 'utf-8') as file:
        num_chars = file.write(text)
        return num_chars
