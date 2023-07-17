#!/usr/bin/python3
"""A rectangle class that inherits from the base class"""
from models.base import Base


class Rectangle(Base):
    """
    A rectangle class
    inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        "initializing the rectangle class instance"
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        "getting the width property"
        return self.__width

    @width.setter
    def width(self, value):
        "setting the width property"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        "getting the height property"
        return self.__height

    @height.setter
    def height(self, value):
        "setting the height property"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        "getting the x property"
        return self.__x

    @x.setter
    def x(self, value):
        "setting the x property"
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        "getting the y property"
        return self.__y

    @y.setter
    def y(self, value):
        "setting the y property"
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        "calculares rectangle class area"
        return self.__height * self.__width

    def display(self):
        "display representation of the rectangle class"
        ll = self.height
        b = self.width
        for a in range(self.y):
            print()
        for i in range(ll):
            for z in range(self.x):
                print(" ", end="")
            for j in range(b):
                print("#", end="")
            print()

    def __str__(self):
        "modifying string representation of class"
        ret = "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)
        return ret

    def update(self, *args, **kwargs):
        "introducing an update method"
        if args is not None and len(args) != 0:
            update_list = []
            for arg in args:
                update_list.append(arg)
            if len(update_list) != 0:
                self.id = update_list[0]
            if len(update_list) > 1:
                self.width = update_list[1]
            if len(update_list) > 2:
                self.height = update_list[2]
            if len(update_list) > 3:
                self.x = update_list[3]
            if len(update_list) > 4:
                self.y = update_list[4]
        else:
            my_dict = {}
            for k, v in kwargs.items():
                my_dict.update({k: v})
            if 'id' in my_dict:
                self.id = my_dict['id']
            if "width" in my_dict:
                self.width = my_dict['width']
            if "height" in my_dict:
                self.height = my_dict['height']
            if 'x' in my_dict:
                self.x = my_dict['x']
            if 'y' in my_dict:
                self.y = my_dict['y']

    def to_dictionary(self):
        "returning dictionary representation of class"
        class_dict = {}
        for key, value in self.__dict__.items():
            if key.startswith("_"):
                class_dict[key.split("__")[-1]] = value
            else:
                class_dict[key] = value
        return class_dict
