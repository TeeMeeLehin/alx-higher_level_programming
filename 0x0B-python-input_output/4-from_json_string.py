#!/usr/bin/python3
"function that retruns object from json"
import json


def from_json_string(my_str):
    "returns object represented by json"
    return json.loads(my_str)
