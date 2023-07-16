#!/usr/bin/python3
"""A square class that inherits from the rectangle class"""
from base import Base
from rectangle import Rectangle


class Square(Rectangle):
    """
    A square class
    inherits from rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        "initializing the square class"
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "modifying string representation of class"
        ret = "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)
        return ret

    @property
    def size(self):
        "method to get square size"
        return self.width
    
    @size.setter
    def size(self, value):
        "method to set square size"
        self.width = value
        self.height = value
