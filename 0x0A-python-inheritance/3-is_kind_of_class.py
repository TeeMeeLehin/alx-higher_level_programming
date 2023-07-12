#!/usr/bin/python3
"function to compare 2 class instances"


def is_kind_of_class(obj, a_class):
    "comparing two class instances"
    if isinstance(obj, a_class):
        return True
    else:
        return False
