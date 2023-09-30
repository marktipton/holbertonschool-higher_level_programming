#!/usr/bin/python3
"""Creates rectangle class which inherits from base"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """rectangle class child of base"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width=size, height=size)
