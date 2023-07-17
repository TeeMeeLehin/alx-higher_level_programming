#!/usr/bin/python3
"""base python script"""
import json


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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        "returning json from dictionaries"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        "method to save json obj to file"
        if list_objs is None:
            with open(cls.__name__ + ".json", "w") as file:
                file.write("[]")
        else:
            list_instance = [i.to_dictionary() for i in list_objs]
            with open(cls.__name__ + ".json", "w") as file:
                file.write(cls.to_json_string(list_instance))

    @staticmethod
    def from_json_string(json_string):
        "loading data from json string"
        if json_string is None or json_string == [] or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        "returning class obj from dictionary"
        if cls.__name__ == "Rectangle":
            rect = cls(3, 4)
        elif cls.__name__ == "Square":
            rect = cls(3)
        rect.update(**dictionary)
        return rect
