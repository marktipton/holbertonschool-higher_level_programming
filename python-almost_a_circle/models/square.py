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

    @property
    def size(self):
        """gets size attribute of square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets width and height to same size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an arg to each square attribute"""
        if len(args) >= 1:
            setattr(self, 'id', args[0])
        if len(args) >= 2:
            setattr(self, 'size', args[1])
        if len(args) >= 3:
            setattr(self, 'x', args[2])
        if len(args) >= 4:
            setattr(self, 'y', args[3])
        for key, value in kwargs.items():
            setattr(self, key, value)
