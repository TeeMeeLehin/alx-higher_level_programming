#!/usr/bin/python3
"function to append to file"


def append_write(filename="", text=""):
    "appending to file"
    with open(filename, 'a', encoding="utf-8") as f:
        re = f.write(text)
    return re
