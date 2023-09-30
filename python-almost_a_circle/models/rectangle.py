#!/usr/bin/python3
"""Creates rectangle class which inherits from base"""

from models.base import Base


class Rectangle(Base):
    """rectangle class child of base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """calculate area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints rectangle of # to stdout"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """return string rep of rectangle"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """assigns an arg to each rectangle attribute"""
        if len(args) >= 1:
            setattr(self, 'id', args[0])
        if len(args) >= 2:
            setattr(self, 'width', args[1])
        if len(args) >= 3:
            setattr(self, 'height', args[2])
        if len(args) >= 4:
            setattr(self, 'x', args[3])
        if len(args) >= 5:
            setattr(self, 'y', args[4])
        for key, value in kwargs.items():
            setattr(self, key, value)
