#!/usr/bin/python3
"function to create obj from json file"
import json


def load_from_json_file(filename):
    "function to create object from json file"
    with open(filename) as f:
        fe = f.read()
    return json.loads(fe)
