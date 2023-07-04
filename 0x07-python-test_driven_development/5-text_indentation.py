#!/usr/bin/python3
"""
Function to add Integers


"""


def text_indentation(text):
    """print_square
        text - input string
        """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print("")
            i += 2
        else:
            print(text[i], end="")
            i += 1
