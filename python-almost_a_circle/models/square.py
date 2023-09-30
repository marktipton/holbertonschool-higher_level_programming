#!/usr/bin/python3
"""Creates square class which inherits from rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class child of rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x, y, id)
