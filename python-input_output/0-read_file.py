#!/usr/bin/python3
"""reads a text file and prints it to stdout"""


def read_file(filename=""):
    """reads file and prints it"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
