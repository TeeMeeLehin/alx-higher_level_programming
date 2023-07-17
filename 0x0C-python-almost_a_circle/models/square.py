#!/usr/bin/python3
"""A square class that inherits from the rectangle class"""
from models.rectangle import Rectangle


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

    def update(self, *args, **kwargs):
        "introducing an update method"
        if args is not None and len(args) != 0:
            update_list = []
            for arg in args:
                update_list.append(arg)
            if len(update_list) != 0:
                self.id = update_list[0]
            if len(update_list) > 1:
                self.size = update_list[1]
            if len(update_list) > 2:
                self.x = update_list[2]
            if len(update_list) > 3:
                self.y = update_list[3]
        else:
            my_dict = {}
            for k, v in kwargs.items():
                my_dict.update({k: v})
            if 'id' in my_dict:
                self.id = my_dict['id']
            if "size" in my_dict:
                self.size = my_dict['size']
            if 'x' in my_dict:
                self.x = my_dict['x']
            if 'y' in my_dict:
                self.y = my_dict['y']

    def to_dictionary(self):
        "returning dictionary representation of class"
        class_dict = super().to_dictionary()
        class_dict["size"] = class_dict["width"]
        del class_dict["width"], class_dict["height"]
        return class_dict
