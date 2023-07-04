#!/usr/bin/python3
"""
Function to add Integers


"""


def print_square(size):
    """print_square
        size - length of the square
        """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("{}".format(size * '#'))
        if size == 0:
            print("")
