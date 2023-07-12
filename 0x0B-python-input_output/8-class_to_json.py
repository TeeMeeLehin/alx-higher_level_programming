#!/usr/bin/python3
"functions that returns json from class obj"


def class_to_json(obj):
    "json from class object"
    return obj.__dict__
