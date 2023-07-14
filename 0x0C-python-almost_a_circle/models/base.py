#!/usr/bin/python3
"""base python script"""


class Base():
    """
        Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        "function to initialize the class"
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
