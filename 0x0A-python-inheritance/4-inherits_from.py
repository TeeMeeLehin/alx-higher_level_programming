#!/usr/bin/python3
"function to compare 2 class instances"


def inherits_from(obj, a_class):
    "comparing two class instances"
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
