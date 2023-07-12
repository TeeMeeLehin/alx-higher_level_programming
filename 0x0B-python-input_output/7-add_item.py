#!/usr/bin/python3
"script to add list arguments and save to file"
import sys

if __name__ == "__main__":
    save_func = __import__("5-save_to_json_file").save_to_json_file
    load_func = __import__("6-load_from_json_file").load_from_json_file
    args = sys.argv
    args = args[1:]
    try:
        items = load_func("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(args)
    save_func(items, "add_item.json")
