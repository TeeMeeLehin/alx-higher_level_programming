#!/usr/bin/python3
"function to read a file"

def read_file(filename=""):
    "printing file content to stdout"
    with open(filename) as f:
        for line in f:
            print(line, end="")
