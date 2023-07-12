#!/usr/bin/python3
"function to check if isinstance"


def is_same_class(obj, a_class):
    "function to check if obj is a subclass of aclass"
    if type(obj) == a_class:
        return True
    else:
        return False
