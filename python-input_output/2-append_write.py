#!/usr/bin/python3
""""appends text to a file"""


def append_write(filename="", text=""):
    """appends text to a file"""
    with open(filename, 'a', encoding='utf-8') as file:
        chars_appended = file.write(text)
        return chars_appended
