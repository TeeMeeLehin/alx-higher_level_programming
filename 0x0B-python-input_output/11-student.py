#!/usr/bin/python3
"student class to json with filter"


class Student():
    """Instance of a square class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs is None):
            return self.__dict__
        else:
            return {attr: self.__dict__[attr] for attr
                    in attrs if attr in self.__dict__}

    def reload_from_json(self, json):
        for i, j in json.items():
            setattr(self, i, j)
