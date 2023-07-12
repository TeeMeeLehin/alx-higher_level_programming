#!/usr/bin/python3
"function to return list of available attributes"


def lookup(obj):
    "returns attributes of obj"
    return list(dir(obj))
