#!/usr/bin/python3
"function to save json object to file"
import json


def save_to_json_file(my_obj, filename):
    "function to save json to file"
    with open(filename, 'w', encoding="utf-8") as f:
        re = f.write(json.dumps(my_obj))
    return re
