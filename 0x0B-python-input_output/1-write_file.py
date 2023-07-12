#!/usr/bin/python3
"function to write to a file"


def write_file(filename="", text=""):
    "writing to file"
    with open(filename, 'w', encoding="utf-8") as f:
        re = f.write(text)
    return re
