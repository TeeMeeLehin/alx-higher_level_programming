#!/usr/bin/python3
"appending text to file"


def append_after(filename="", search_string="", new_string=""):
    "function to append text to file  after a particular line"
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as n:
        n.write(text)
