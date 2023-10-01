#!/usr/bin/python3
"""Creates square class which inherits from rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class child of rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
       """return string rep of rectangle"""
       return (
           f"[Square] ({self.id}) {self.x}/{self.y} - "
           f"{self.width}"
        )
